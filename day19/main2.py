
designs = []
patterns = []
usable = []

def parse(fileName):
    global patterns
    file = open(fileName,"r").read().split("\n")
    patterns = file[0].split(", ")
    for x in range(len(file)):
        if file[x] == "" or x == 0:
            continue
        designs.append(file[x])
    #patterns.sort(key=len,reverse=True)
def check(index):

    def isGut(gut,index,iter):
        
        used = gut[index][iter]
        usedLen = len(patterns[used])
        if usedLen <= 0:
            return False

        index += usedLen
        print(index,iter)


        if index == len(gut):
            return True

        if index > len(gut):
            return False

        holder = 0
        for x in range(len(gut[index])):
            holder += isGut(gut,index,x)
        #print(index,gut[index])

        #for x in range(len(gut[index])):
        #    print(x,indexD)
        #    holder+=isGut(gut,gut[index][x],index,x)
        return holder

    used = designs[index]
    print(used)
    gut = []
    for x in range(len(used)):
        gut.append([])

    for x in range(len(used)):
        for y in range(len(patterns)):
            for z in range(len(patterns[y])):
                if z+x >= len(used):
                    break
                if used[x+z] != patterns[y][z]:
                    break
                if z+1 == len(patterns[y]):
                    gut[x].append(y)
    for x in gut:
        for y in x:
            print(patterns[y],end=",")
        print("|",end="")
    print("")
    print(gut)
    for x in range(len(gut[0])):
        print("DD")
        hold = isGut(gut,0,x)
        if hold > 0:
            usable.append(gut)
            print("hold: ",hold)
            return hold
    return False

#Dać by zwracało indexy z patterns które można złożyć z kilku pomniejszysz
def getCompositeIndexes():
    composite = []
    return composite
def printGut():
    for x in usable:
        True
parse("input1.txt")
score = 0
print(patterns)
for x in range(len(designs)):
    print("add")
    score += check(x)
print("Score: ",score)
