from PIL import Image

map = []
mapSize = [0,0]
moveList = []
gamer = [-1,-1]
lookUp = [">","<","v","^"]
changed = True

def genMap(show = False,save=False,fileName="./img.bmp"):
    global map
    
    img = Image.new("RGB",(mapSize[0],mapSize[1]),"black")
    colorDict = {".":(100,100,100),"#":(0,0,0),"O":(0,255,0),"[":(0,255,100),"]":(100,255,0)}
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

    map[y] = map[y][:-(mapSize[0]-x)]+sym+(map[y][x+1:])

def parse(fileName):
    global map
    global moveList
    global gamer
    global changed

    file = open(fileName,"r").read().split("\n")
    state = 0
    hashMap = {">" : 0,"<":1,"v":2,"^":3}
    holder = ""

    for y in range (len(file)):
        if file[y] == "":
            state+=1

        if state == 0:
            holder = "##"
            #map.append(["##"])

        for x in range(len(file[y])):
            if state == 0 and x == 0:
                continue
            match state:
                case 0:
                    if file[y][x] == "@":
                        gamer[0]=len(holder)
                        gamer[1]=y
                        holder+=".."
                    elif file[y][x] == "#":
                        holder+="##"
                    elif file[y][x] == "O":
                        holder+="[]"
                    else:
                        holder+=".."
                case 1:
                    moveList.append(str(hashMap[file[y][x]]))
                case 2:
                    return
        if state == 0:
            map.append(holder)
            mapSize[1] = len(map)
            mapSize[0] = len(map[0])

def move():
    global map
    global moveList
    global gamer
    global lookUp
    def blockMoveEx(x,y,command):
        global map
        if map[y][x] == ".":
            return True
        if map[y][x] == "#":
            return False
        moveTable = [[1,0],[-1,0],[0,1],[0,-1]]
        next = [x+moveTable[command][0],y+moveTable[command][1]]
        px = -1
        py = -1
        used = ["",""]
        if map[y][x] == "[":
            used = ["[","]"]
            px = x+1
            py = y
        if map[y][x] == "]":
            used = ["]","["]
            px = x-1
            py = y
        pnext = [px+moveTable[command][0],py+moveTable[command][1]]

        if map[next[1]][next[0]] == "#" or map[pnext[1]][pnext[0]] == "#":
            return False

        if [px,py] == next and map[pnext[1]][pnext[0]] == ".":
                return True
        if [px,py] == next and (map[pnext[1]][pnext[0]] == "[" or map[pnext[1]][pnext[0]] == "]"):
            if blockMoveEx(pnext[0],pnext[1],command):
                return True

        if map[next[1]][next[0]] == "." and map[pnext[1]][pnext[0]] == ".":
                return True
        if [px,py] != next and((map[next[1]][next[0]] == "[" or map[next[1]][next[0]] == "]") or (map[pnext[1]][pnext[0]] == "[" or map[pnext[1]][pnext[0]] == "]")):
            if blockMoveEx(next[0],next[1],command) and blockMoveEx(pnext[0],pnext[1],command):
                    return True
        if command == 1 and (map[pnext[1]][pnext[0]] == "[" or map[pnext[1]][pnext[0]] == "]"):
            if blockMove(pnext[0],pnext[1],command):
                return False
    def blockMove(x,y,command):
        global map
        if map[y][x] == ".":
            return True
        if map[y][x] == "#":
            return False
        moveTable = [[1,0],[-1,0],[0,1],[0,-1]]
        next = [x+moveTable[command][0],y+moveTable[command][1]]
        px = -1
        py = -1
        used = ["",""]
        if map[y][x] == "[":
            used = ["[","]"]
            px = x+1
            py = y
        if map[y][x] == "]":
            used = ["]","["]
            px = x-1
            py = y
        pnext = [px+moveTable[command][0],py+moveTable[command][1]]

        if map[next[1]][next[0]] == "#" or map[pnext[1]][pnext[0]] == "#":
            return False

        if [px,py] == next and map[pnext[1]][pnext[0]] == ".":
                replace(x,y,".")
                replace(px,py,".")
                replace(next[0],next[1],used[0])
                replace(pnext[0],pnext[1],used[1])
                return True
        if [px,py] == next and (map[pnext[1]][pnext[0]] == "[" or map[pnext[1]][pnext[0]] == "]"):
            if blockMoveEx(pnext[0],pnext[1],command):
                blockMove(pnext[0],pnext[1],command)
                replace(x,y,".")
                replace(px,py,".")
                replace(next[0],next[1],used[0])
                replace(pnext[0],pnext[1],used[1])
                return True

        if map[next[1]][next[0]] == "." and map[pnext[1]][pnext[0]] == ".":

                replace(x,y,".")
                replace(px,py,".")
                replace(next[0],next[1],used[0])
                replace(pnext[0],pnext[1],used[1])
                return True
        if [px,py] != next and((map[next[1]][next[0]] == "[" or map[next[1]][next[0]] == "]") or (map[pnext[1]][pnext[0]] == "[" or map[pnext[1]][pnext[0]] == "]")):
            if blockMoveEx(next[0],next[1],command) and blockMoveEx(pnext[0],pnext[1],command):
                    blockMove(next[0],next[1],command)
                    blockMove(pnext[0],pnext[1],command)
                    replace(x,y,".")
                    replace(px,py,".")
                    replace(next[0],next[1],used[0])
                    replace(pnext[0],pnext[1],used[1])

                    return True
        if command == 1 and (map[pnext[1]][pnext[0]] == "[" or map[pnext[1]][pnext[0]] == "]"):
            if blockMove(pnext[0],pnext[1],command):
                    replace(x,y,".")
                    replace(px,py,".")
                    replace(next[0],next[1],used[0])
                    replace(pnext[0],pnext[1],used[1])

                    return True
        #print(px,py,[px,py] != next , map[next[1]][next[0]] == "[" or map[next[1]][next[0]] == "]")
        #genMap(save=True,fileName="./img/"+str(x)+str(y)+lookUp[command]+".bmp")

        return False

    usedMove = int(moveList.pop(0))
    #print(usedMove)
    moveTable = [[1,0],[-1,0],[0,1],[0,-1]]
    next = [gamer[0]+moveTable[usedMove][0],gamer[1]+moveTable[usedMove][1]]
    if blockMove(next[0],next[1],usedMove):
        #print(gamer)
        gamer[0] = next[0]
        gamer[1] = next[1]
    #print(next,usedMove)

def getBoxes():
    boxes = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "[":
                boxes.append([x,y])
    return boxes

parse("input.txt")

#print(moveList)
genMap(save=True,fileName="./img/"+str(0)+".bmp")
for x in range(len(moveList)):
    move()
    #genMap(save=True,fileName="./img/"+str(x+1)+".bmp")

score =0
for x in getBoxes():
    score+=(x[1]*100+x[0])

print("Score: ",score,len(getBoxes()))
