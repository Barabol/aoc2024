
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
    patterns.sort(key=len,reverse=True)
def check(index):

    def isGut(gut,index,iter,strHolder,strWorked,strIters,before = ""):
        
        used = gut[index][iter]
        usedLen = len(patterns[used])
        if usedLen <= 0:
            return False

        index += usedLen
        uStr = before+patterns[used]
        #print(uStr)
        if uStr in strHolder:
            strIters[strHolder.index(uStr)]+=1
            return False
        strHolder.append(uStr)
        strIters.append(0)
        if index == len(gut):
            strWorked.append(1)
            return True

        if index > len(gut):
            strWorked.append(0)
            return False

        holder = 0
        for x in range(len(gut[index])):
            holder += isGut(gut,index,x,strHolder,strWorked,strIters,uStr)

        strWorked.append(holder)
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
    print("gut = ",gut)
    print("patterns = ",patterns)
    for x in patterns:
        if len(x) <= 0:
            return False
    a = []
    b = []
    c = []
    for x in range(len(gut[0])):
        print("DD")
        hold = isGut(gut,0,x,a,b,c)
        if hold > 0:
            usable.append(gut)
            print("hold: ",hold)
            print("strs:",a,"\nWorked: ",b,"\nIters: ",c)
            for z in range(len(b)):
                if c[z] > 0:
                    hold+=c[z]*b[z]
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
