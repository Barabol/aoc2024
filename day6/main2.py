import os
import time 
class holder:
    UP=0
    DOWN=2
    LEFT=3
    RIGHT=1
map = []#  x y
mapSize = [0,0]
#        x y gdzie patrzy
guard = [0,0,holder.UP]
guardHolder = []
score=0
relScore = []
bounces=[]
blanks = []

def addToScore(x,y):
    for z in relScore:
        if z[0] == x and z[1] == y:
            return
    relScore.append([x,y])

def addBounce(x,y):
    global score
    for z in bounces:
        if z[0] == x and z[1] == y and guard[2] == z[2]:
            score+=1
            print("He?",bounces)
            printMap()
            return True
    bounces.append([x,y,guard[2]])
    return False

def printMap():
    gamer = "\033[1m󰣇\033[0m"
    for x in range(len(map)):
        if(x == guard[1]):
            if(map[x][guard[1]] == "."):
                print(map[x][:-(mapSize[0]-guard[0])]+(map[x][guard[0]:]).replace(".",gamer,1))
            elif(map[x][guard[1]] == "x"):
                print(map[x][:-(mapSize[0]-guard[0])]+(map[x][guard[0]:]).replace("x",gamer,1))
        else:
            print(map[x])
    print("Guard: ",guard)

def genMap():
    global guard
    global map
    global mapSize
    file = open("input.txt","r").read().split("\n")
    noGuard=True
    mapSize = [len(file[0]),len(file)]
    mapSize[1] -=1;
    for x in range(len(file)):
        if file[x] == "\n":
            break
        map.append(file[x])
        if noGuard==True:
            for y in range (len(file[x])):
                if file[x][y] == "^":
                    map[x] = map[x].replace("^",".")
                    noGuard = False
                    guard=[y,x,guard[2]] # ależ kocham to jak pisze nestowane pętle
                    break
def replace(x,y,sym="x"):
    global map
    map[y] = map[y][:-(mapSize[0]-x)]+(map[y][x:]).replace(".",sym,1)

def getBlanks():
    global map
    global mapSize
    global blanks

    for x in range(mapSize[0]):
        for y in range(mapSize[1]):
            if map[y][x]=="." and not (x == guard[0] and y == guard[1]):
                blanks.append([x,y])

def move():
    global guard
    global map 
    global mapSize 
    global score 

    getLoc=[0,0]
    match(guard[2]):
        case holder.UP:
            getLoc[1]=-1
        case holder.DOWN:
            getLoc[1]=1
        case holder.LEFT:
            getLoc[0]=-1
        case holder.RIGHT:
            getLoc[0]=1
    #print(mapSize)
    #print(guard[0]+getLoc[0],guard[1]+getLoc[1])
    if guard[0]+getLoc[0]>=mapSize[0] or guard[1]+getLoc[1]>=mapSize[1] or guard[0]+getLoc[0] < 0 or guard[1]+getLoc[1] < 0:
        return True
    if map[guard[1]+getLoc[1]][guard[0]+getLoc[0]] != "#":
        replace(guard[0],guard[1])
        addToScore(guard[0],guard[1])
        guard=[guard[0]+getLoc[0],guard[1]+getLoc[1],guard[2]]
        #score zmienić na tablice z intami i wstawiać do niej mapSize[1]*y + x
        #i potem przy dodawaniu sprawdzać czy jdst unikatowe
        #ALBO TABELE 2 wymiarową z wszystkimi punktami unikatowymi co zaoszczędzi na pamięci
        #ale python to język dla dzieci i nie jest wydajny
        return False
    else:
        #printMap()
        #os.system("clear")
        if addBounce(guard[0],guard[1])==True:
            bounces.clear()
            print(bounces)
            return True
        if guard[2] != 3:
            guard[2]+=1
        else:
            guard[2]=0
        return False

def tryPlacement(x,y):
    global map
    global bounces
    global guardHolder
    global guard

    mapCpy = map.copy()
    replace(x,y,"#")
    while move() != True:
        True
    map = mapCpy.copy()
    bounces.clear()
    #printMap()
    guard = guardHolder

genMap()
getBlanks()
# bruteforce? może?
# zapisywać odbicia i sprawdzić czy dochodzi do duplikacji 

print(len(blanks),blanks)
guardHolder = guard.copy()
for x in blanks:
    print("Trying: ",x)
    tryPlacement(x[0],x[1])
    guard = guardHolder.copy()

tryPlacement(2,6)
printMap()
print("Score: ",score)

