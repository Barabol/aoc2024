import re
import sys
from PIL import Image
sys.setrecursionlimit(15000)
bytePos = []
map = []
def genMap(show = False,save=False,fileName="./img.bmp"):
    global map
    img = Image.new("RGB",(mapSize[0]+1,mapSize[1]+1),"black")
    colorDict = {0:(100,100,100),1:(255,0,0),2:(0,255,0),3:(0,0,255)}
    pixels = img.load()
    for y in range(mapSize[1]+1):
        for x in range(mapSize[0]+1):
            pixels[x,y] = colorDict[map[y][x]]
    if show:
        img.show()

    if save:
        img.save(fileName)
def help():
    for y in range(mapSize[1]+1):
        for x in range(mapSize[0]+1):
            if map[y][x] == 0:
                print(".",end="")
            else:
                print("#",end="")
        print()
def parse(fileName):
    file = open(fileName,"r")
    counter = 0
    for x in file:
        if counter == 1024:
            return
        bytePos.append([int(re.findall(r"\d+",x)[0]),int(re.findall(r"\d+",x)[1])])
        map[int(re.findall(r"\d+",x)[1])][int(re.findall(r"\d+",x)[0])] = 1
        counter+=1

def fillMap():
    for y in range(mapSize[1]+1):
        map.append([])
        for x in range(mapSize[0]+1):
            map[y].append(0)

def move(x,y,bx,by):
    if x == bx and y == by:
        return 0
    if x > mapSize[0] or y > mapSize[1] or y<0 or x<0:
        return 0
    if map[y][x] != 0 and map[y][x] !=3:
        return 0
    if x == mapSize[0] and y == mapSize[1]:
        map[y][x]=3
        return 1
    map[y][x]=2
    holder = 1
    cloaserX=0 
    cloaserY=0
    if x>mapSize[0]:
        cloaserX = -1
    else:
        cloaserX = 1
    if y>mapSize[1]:
        cloaserY = -1
    else:
        cloaserY = 1
    holder = move(x+cloaserX,y,x,y)
    if holder > 0:
        map[y][x]=3
        return 1+holder
    holder = move(x,y+cloaserY,x,y)
    if holder > 0:
        map[y][x]=3
        return 1+holder

    holder = 1
    holder1 = [0,0,0,0]
    holder1[0] = move(x+1,y,x,y)
    holder1[1] = move(x-1,y,x,y)
    holder1[2] = move(x,y-1,x,y)
    holder1[3] = move(x,y+1,x,y)
    holder1.sort()
    for z in holder1:
        if z >0:
            holder+=z
            break
    if holder > 1:
        map[y][x]=3
        return holder
    return 0
    
# dla input1 6,6 dla input 70,70
mapSize = [70,70]
fillMap()
parse("input.txt")
print(bytePos,"\n",map)
for x in bytePos:
    print(x)
print("Score: ",move(0,0,0,-1)-1)
genMap(show = True)
#help()
