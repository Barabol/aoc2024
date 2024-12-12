map = []
binaryMap = [[]]
binaryMapCpy = [[]]
mapSize = [0,0]
used = 0

def parse():
    global map
    global mapSize
    global binaryMap
    global binaryMapCpy

    map = open("input.txt","r").read().split("\n")
    map.pop()
    
    mapSize[0] = len(map[0])
    mapSize[1] = len(map)
    
    for x in range(mapSize[0]):
        binaryMap[0].append(False)
        binaryMapCpy[0].append(False)


    for x in range(mapSize[1]-1):
        binaryMap.append(binaryMap[0].copy())
        binaryMap.append(binaryMapCpy[0].copy())

    binaryMapCpy = binaryMap.copy()

def printBm(a):
    for x in a:
        for y in x:
            if y:
                print("#",end="")
            else:
                print(".",end="")
        print()
    print()

def scan(x,y):# zrobić to rekurencją
    global used

    def getBinary(bMap):
        score = 0
        for x in bMap:
            #print(x)
            for y in x:
                score+=y
        #printBm(bMap)
        return score
    
    def scanEx(x,y,char,bMap):#przecież moge to tu wykryć ile płotków jest essa
        global used
        if x<0 or x>= mapSize[0] or  y<0 or y>= mapSize[1]:
            return 1
        if bMap[y][x]:
            return 0
        if map[y][x] == char:
            bMap[y][x] = True
            used+=1
            binaryMap[y][x] = True

            catcher = 0
            catcher += scanEx(x+1,y,char,bMap)
            catcher += scanEx(x-1,y,char,bMap)
            catcher += scanEx(x,y+1,char,bMap)
            catcher += scanEx(x,y-1,char,bMap)
            return catcher
        else:
            return 1
    
    if(binaryMap[y][x] == True):
        return [-1,-1]
    holder = [[]]
    for z in range(mapSize[0]):
        holder[0].append(False)

    for z in range(mapSize[1]-1):
        holder.append(holder[0].copy())

    char = map[y][x]
    used = 0
    #printBm(holder)
    return [scanEx(x,y,char,holder),used,char,x,y]

parse()
for x in map:
    print(x)
#for x in binaryMap:
#    print(x)
tab = []
for y in range(mapSize[1]):
    for x in range(mapSize[0]):
        holder = scan(x,y)
        if holder[0] != -1:
            tab.append(holder)

score = 0
for x in tab:
    print(x)
    score+= x[0]*x[1]

print(score)
