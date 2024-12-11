locs = []
uniqueChars = []
mapSize = [0,0]
antenas = []
file = []

def replace(x,y,sym="x"):
    global file 
    #print(x,y,mapSize)
    if(file[y][x] == "."):
        file[y] = file[y][:-(mapSize[0]-x)]+(file[y][x:]).replace(".",sym,1)
def getVal(x,y):
    global locs
    for z in locs:
        if z[0] == x and z[1] == y:
            return z[2]

    return -1

def addAntena(x,y,char):
    global antenas
    for z in antenas:
        if x == z[0] and y == z[1]:
            return
    #if getVal(x,y) == char:
    #   return
    replace(x,y,"#")
    antenas.append([x,y])

def getValues(char):
    vals = []
    if char == -1:
        return vals
    for x in locs:
        if x[2] == char:
            vals.append([x[0],x[1]])
    return vals

def parse():

    global file
    def addChar(char):
        global uniqueChars
        for z in uniqueChars:
            if char == z:
                return
        uniqueChars.append(char)

    def add(x,y,char):
        global locs
        for z in locs:
            if z[2] == char and z[0] == x and z[1] == y:
                return
        locs.append([x,y,char])


    file = open("input.txt","r").read().split("\n")
    
    mapSize[1] = len(file[0])
    mapSize[0] = len(file)-1

    for y in range(len(file)):
        for x in range(len(file[y])):
            if file[y][x] != '.':
                add(x,y,file[y][x])
                addChar(file[y][x])
def tryComb(x,char,xOff,yOff,gg):
    if (gg == 0 or gg == 1) and not ((x[0]-xOff)<0  or (x[1]-yOff)<0 or (x[0]-xOff)>=mapSize[0] or (x[1]-yOff)>=mapSize[1]):
        #print(char,"a[",x[0]-xHolder,x[1]-yHolder,"]")
        addAntena(x[0]-xOff,x[1]-yOff,char)
        tryComb([x[0]-xOff,x[1]-yOff],char,xOff,yOff,1)

    if (gg == 0 or gg == 2) and not((xOff+x[0])>=mapSize[0] or (yOff+x[1])>=mapSize[1] or (x[0]+xOff)<0  or (x[1]+yOff)<0):
        #print(char,"b[",x[0]+xHolder,x[1]+yHolder,"]",xHolder,yHolder)
        addAntena(x[0]+xOff,x[1]+yOff,char)
        tryComb([x[0]+xOff,x[1]+yOff],char,xOff,yOff,2)
    return 

def form(char):
    global locs
    xHolder = 0
    yHolder = 0
    used = getValues(char)
    for x in used:
        for y in used:
            if x[0] == y[0] and x[1] == y[1]:
                continue
            #print(x,y)

            xHolder = x[0]-y[0]
            yHolder = x[1]-y[1]
            tryComb(x,char,xHolder,yHolder,0)


parse()
print(locs)
print(uniqueChars)
for x in uniqueChars:
    #print(x)
    form(x)
print(len(antenas)," powinno być 34")
for x in file:
    print(x)
