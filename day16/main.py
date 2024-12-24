from PIL import Image
import sys
from copy import deepcopy

from numpy import right_shift
from numpy.__config__ import show
from numpy._typing import _NBitDouble

mapG = []
mapSize = [0,0]
moveList = []
gamer = [-1,-1]
goal= [-1,-1]
sys.setrecursionlimit(15000)

def genMap(show = False,save=False,fileName="./img.bmp",map=[],point=[-1,-1]):
    
    img = Image.new("RGB",(mapSize[0],mapSize[1]),"black")
    colorDict = {".":[(100,100,100),(110,110,110)],"#":[(0,0,0),(10,10,10)],"O":[(0,255,0),(100,255,100)],"x":[(100,10,100),(255,10,10)]}
    pixels = img.load()
    for y in range(mapSize[1]):
        for x in range(mapSize[0]):
            if gamer[0] == x and gamer[1] == y:
                pixels[x,y] = (100,100,255)
            else:
                pixels[x,y] = colorDict[map[y][x]][(x+y)&1]

    if point[0]!=-1:
        pixels[point[0],point[1]] = (255,0,0)
    if show:
        img.show()

    if save:
        img.save(fileName)

def replace(x,y,sym="x",toReplace=".",map = []):
    global mapSize

    if(map[y][x] == toReplace):
        map[y] = map[y][:-(mapSize[0]-x)]+(map[y][x:]).replace(toReplace,sym,1)
        return True
    return False

def parse(fileName):
    global mapG
    global moveList
    global gamer
    global changed

    file = open(fileName,"r").read().split("\n")
    state = 0
    hashMap = {">" : 0,"<":1,"v":2,"^":3}

    for y in range (len(file)):
        if file[y] == "":
            state+=1

        if state == 0:
            mapG.append(file[y])
            mapSize[1] = len(mapG)
            mapSize[0] = len(mapG[0])

        for x in range(len(file[y])):
            match state:
                case 0:
                    if file[y][x] == "S":
                        gamer[0]=x
                        gamer[1]=y
                        if replace(x,y,sym=".",toReplace="S",map=mapG) == False:
                            print("Co?")
                    if file[y][x] == "E":
                        goal[0]=x
                        goal[1]=y
                        if replace(x,y,sym=".",toReplace="E",map=mapG) == False:
                            print("Co?")

                case 1:
                    moveList.append(hashMap[file[y][x]])
                case 2:
                    return
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
coords = [[],[],[],[]]
coords[UP] = [0,-1]
coords[DOWN] = [0,1]
coords[LEFT] = [-1,0]
coords[RIGHT] = [1,0]

canGo = [[],[],[],[]]
canGo[LEFT] = [coords[DOWN],coords[UP]]
canGo[RIGHT] = [coords[DOWN],coords[UP]]
canGo[UP] = [coords[LEFT],coords[RIGHT]]
canGo[DOWN] = [coords[LEFT],coords[RIGHT]]

canGoNames = [[],[],[],[]]
canGoNames[LEFT] = [DOWN,UP]
canGoNames[RIGHT] = [DOWN,UP]
canGoNames[UP] = [LEFT,RIGHT]
canGoNames[DOWN] = [LEFT,RIGHT]

canGoStr= ["","","",""]
canGoStr[LEFT] = "LEFT"
canGoStr[RIGHT] = "RIGHT"
canGoStr[UP] = "UP"
canGoStr[DOWN] = "DOWN"

def notMoved(x,y,lDir,cDir,locs,map):
    global UP
    global DOWN
    global RIGHT
    global LEFT
    for z in (locs[lDir]):
        if z[0] == x and z[1] == y and z[2] == cDir:
            #print(x,y,canGoStr[lDir])
            return False

    #replace(x,y,"x","O",map)
    locs[lDir].append([x,y,cDir])
    return True

def move(x,y,nDir,movTab,map,locs = [[],[],[],[]]):
    global UP
    global DOWN
    global RIGHT
    global LEFT
    global solutions
    global coords
    global canGo

    if map[y][x] == "#":
        return 

    x+=coords[nDir][0]
    y+=coords[nDir][1]
    created = False
    while map[y][x] != "#":

        #replace(x,y,"O",".",map)
        #print("x: ",x,"y: ",y,"coords: ",coords[nDir],coords[nDir][0] == 0,x+coords[nDir][0])
        if x == goal[0] and y == goal[1]:
            solutions.append([movTab,map])
            print(f"Found {len(solutions)}'th with {movTab[0]+(movTab[1]*1000)} Score")
            #genMap(show=True,map=map)
            return

        for z in range(2):
            if map[y+canGo[nDir][z][1]][x+canGo[nDir][z][0]] == ".":
                if notMoved(x+coords[canGoNames[nDir][z]][0],y+coords[canGoNames[nDir][z]][1],canGoNames[nDir][z],nDir,locs,map):
                    move(x,y,canGoNames[nDir][z],[deepcopy(movTab[0])+1,deepcopy((movTab[1]))+1],deepcopy(map),deepcopy(locs))
                #else:
                    #genMap(show=True,map=map,point=[x+coords[canGoNames[nDir][z]][0],y+coords[canGoNames[nDir][z]][1]])

        x = x + coords[nDir][0]
        y = y + coords[nDir][1]
        movTab[0]+=1

    return
parse("input.txt")
solutions = []
#genMap(show=True)
for x in range(4):
    move(gamer[0],gamer[1],x,[1,1],deepcopy(mapG))
#genMap(show=True)
scores = solutions[0]
holder2 = solutions[0]
holder = holder2[0][0]+(1000*(holder2[0][1]))
for y in solutions:
    #genMap(save=True ,fileName="./img/"+str(y[0][0]+(1000*(y[0][1])))+".png",map=y[1])
    if (y[0][0]+(1000*(y[0][1]))) < holder:
        holder2 = scores
        scores = y
        holder =y[0][0]+(1000*(y[0][1])) 
#print(scores)
print(scores[0][0]+(1000*scores[0][1]))
#genMap(show=True,map=scores[1])
#genMap(show=True,map=holder2[1])

# Dać kopie całej mapy i na niej zaznaczac i potem wypisać będzie łatwiej zobaczyć co się dzieje
