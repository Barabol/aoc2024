import re
from PIL import Image

mapSize = [101,103]
bots = []

def parse(fileName):
    global bots
    file = open(fileName,"r")

    for line in file:
        found = re.findall(r"-?\d+",line)
        found[0] = int(found[0])
        found[1] = int(found[1])
        found[2] = int(found[2])
        found[3] = int(found[3])
        bots.append(found)

def move(index):
    global bots
    global mapSize
    used = bots[index]

    used[0]+=used[2]
    used[1]+=used[3]

    while used[0]<0 or used[1]<0:
        if used[0] < 0:
            used[0]+=mapSize[0]

        if used[1] < 0:
            used[1]+=mapSize[1]

    while used[0]>=mapSize[0] or used[1]>=mapSize[1]:
        if used[0] >= mapSize[0]:
            used[0]-=mapSize[0]

        if used[1] >= mapSize[1]:
            used[1]-=mapSize[1]


    #print(bots[index])

def getValue(iter):
    global bots
    holder = []
    for y in range(mapSize[1]):
        holder.append([])
        for x in range(mapSize[0]):
            holder[y].append(0)
        
    for b in bots:
        holder[b[1]][b[0]]+=1

    halfMap = [mapSize[0]//2,mapSize[1]//2]
    sums = [0,0,0,0]
    img = Image.new( 'RGB', (mapSize[0],mapSize[1]), "black") # create a new black image
    pixels = img.load() # create the pixel map
    for y in range(mapSize[1]):

        for x in range(mapSize[0]):
            #if x == halfMap[0]:
                #print("  ",end="")
            #if x == halfMap[0] or y == halfMap[1]:
                #continue
            
            if holder[y][x] == 0:
                #print(" ",end="")
                True
            else:
                #print("#",end="")
                pixels[x,y] = (0,255,0)
            if y < halfMap[1]:
                if x < halfMap[0]: 
                    sums[0]+=holder[y][x]
                else:
                    sums[1]+=holder[y][x]

            else:
                if x < halfMap[0]: 
                    sums[2]+=holder[y][x]
                else:
                    sums[3]+=holder[y][x]
        print()
    sum = 1
    for x in sums:
        sum*=x
  
    img.save("./images/"+str(iter)+".png") 
    print("Score: ",sum)

parse("input.txt")
for x in range(5000):
    for z in range(len(bots)):
        move(z)
    getValue(1+x)
for x in range(5000):
    for z in range(len(bots)):
        move(z)   
    getValue(50001+x)
