import time
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
            if y == True:
                print("#",end="")
            else:
                print(".",end="")
        print()
    print()

def scan(x,y):# zrobić to rekurencją
    global used

    def getSides(bMap):

        def getUniquesAmm(hold,index):
            uniques = []
            pointer = [len(hold[0])-1,len(hold[1])-1]
            if pointer[0] == -1 and pointer[1] == -1:
                return 0
            uqe = True
            #print("++Unique",index)
            #print(hold)
            while pointer[index] != -1:
                uqe = True
                uzed = pointer[index^1]
                while uzed!=-1:
                    if hold[index][pointer[index]] == hold[index^1][uzed]:
                        uqe = False
                        hold[index^1].pop(uzed)
                        pointer[index^1]-=1
                        #print(hold)
                        break
                    uzed-=1
                pointer[index]-=1
                
                if uqe:
                    uniques.append(hold[index][pointer[index]])
            #print(len(uniques))
            #print("--Unique")
            return len(uniques)

            
        #printBm(bMap)

        sides = 0

        holding = [[],[]]
        #Wertykalne
        for x in range(mapSize[0]):
            holding[x&1] = []
            for y in range(mapSize[1]):
                if bMap[y][x]:
                    if y+1 >= mapSize[1] or holder[y+1][x] == False:
                        holding[x&1].append(str(y)+str(y+1))
                    if y-1 < 0 or holder[y-1][x] == False:
                        holding[x&1].append(str(y)+str(y-1))

            #print(holding,len(holding[x&1]))
            sides+= getUniquesAmm(holding,x&1)
        #print("Horizontal")
        holding = [[],[]]
        #print(sides)
        #sides = 0

        #Horyzontalne
        for y in range(mapSize[1]):
            holding[y&1] = []
            for x in range(mapSize[0]):
                if bMap[y][x]:
                    if x+1 >= mapSize[0] or holder[y][x+1] == False:
                        holding[y&1].append(str(x)+str(x+1))
                    if x-1 < 0 or holder[y][x-1] == False:
                        holding[y&1].append(str(x)+str(x-1))

            #print(holding,len(holding[x&1]))
            sides+= getUniquesAmm(holding,y&1)
            
        holding = [[],[]]
        if sides&1:
            print(sides)
            printBm(holder)
            sides+=1

        return sides
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
    scanEx(x,y,char,holder)
    return [used,getSides(holder),char,x,y]
def run():
    gg = time.time()
    tab = []
    for y in range(mapSize[1]):
        for x in range(mapSize[0]):
            holder = scan(x,y)
            if holder[0] != -1:
                tab.append(holder)

    score = 0
    for x in tab:
        #print(x)
        score+= x[0]*x[1]
    print(time.time()-gg)
    print(score)


parse()
run()
#print(scan(0,0))


#for x in map:
    #print(x)
#for x in binaryMap:
#    print(x)

