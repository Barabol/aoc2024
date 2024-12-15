from os import times_result
from PIL import Image

map = []
mapSize = [0,0]
moveList = []
gamer = [-1,-1]
lookUp = [">","<","v","^"]

def genMap(show = False,save=False,fileName="./img.bmp"):
    global map
    
    img = Image.new("RGB",(mapSize[0],mapSize[1]),"black")
    colorDict = {".":(100,100,100),"#":(0,0,0),"O":(0,255,0)}
    pixels = img.load()
    for y in range(mapSize[1]):
        for x in range(mapSize[0]):
            if gamer[0] == x and gamer[1] == y:
                pixels[x,y] = (100,100,255)
            else:
                pixels[x,y] = colorDict[map[y][x]]
    if show:
        img.show()

    if save:
        img.save(fileName)

def replace(x,y,sym="x",toReplace="."):
    global map
    global mapSize

    if(map[y][x] == toReplace):
        map[y] = map[y][:-(mapSize[0]-x)]+(map[y][x:]).replace(toReplace,sym,1)
        return True
    return False

def parse(fileName):
    global map
    global moveList
    global gamer

    file = open(fileName,"r").read().split("\n")
    state = 0
    hashMap = {">" : 0,"<":1,"v":2,"^":3}

    for y in range (len(file)):
        if file[y] == "":
            state+=1

        if state == 0:
            map.append(file[y])
            mapSize[1] = len(map)
            mapSize[0] = len(map[0])

        for x in range(len(file[y])):
            match state:
                case 0:
                    if file[y][x] == "@":
                        gamer[0]=x
                        gamer[1]=y
                        if replace(x,y,sym=".",toReplace="@") == False:
                            print("Co?")
                case 1:
                    moveList.append(hashMap[file[y][x]])
                case 2:
                    return

def move():
    global map
    global moveList
    global gamer
    global lookUp
    def tryBlockMove(x,y,command):
        if map[y][x] == ".":
            return True
        if map[y][x] == "#":
            return False

        moveTable = [[1,0],[-1,0],[0,1],[0,-1]]
        usedMove = [x+moveTable[command][0],y+moveTable[command][1]]

        if map[usedMove[1]][usedMove[0]] == "#":
            return False

        if map[usedMove[1]][usedMove[0]] == ".":
            #def replace(x,y,sym="x",toReplace="."):
            (replace(x,y,".","O"))
            (replace(usedMove[0],usedMove[1],"O","."))
            return True 

        if map[usedMove[1]][usedMove[0]] == "O":
            if tryBlockMove(usedMove[0],usedMove[1],command):
                replace(x,y,".","O")
                replace(usedMove[0],usedMove[1],"O",".")
                return True 

        return False

    usedMove = moveList.pop(0)
    moveTable = [[1,0],[-1,0],[0,1],[0,-1]]
    #print(lookUp[usedMove])
    next = [gamer[0]+moveTable[usedMove][0],gamer[1]+moveTable[usedMove][1]]

    if tryBlockMove(next[0],next[1],usedMove):
        gamer = next

    #print(next)

def getBoxes():
    boxes = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "O":
                boxes.append([x,y])
    return boxes

parse("input.txt")


for x in range(len(moveList)):
    move()

genMap(save=True,fileName="./img/"+str(1)+".bmp")
score =0
for x in getBoxes():
    score+=(x[1]*100+x[0])

print("Score: ",score)
