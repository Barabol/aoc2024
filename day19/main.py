
designs = []
patterns = []

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

    def isGut(gut,val,index):
        usedLen = len(patterns[val])
        if usedLen == 0:
            return False
        index += usedLen
        if index == len(gut):
            return True

        if index > len(gut):
            return False

        holder = 0
        print(index,gut[index])
        for x in gut[index]:
            if index == 0 and isGut(gut,x,index):
                holder+=1

        if holder > 0:
            return True
        return False
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
                
    print(gut)
    for x in gut[0]:
        if isGut(gut,x,0):
            return True
    return False
parse("input.txt")
score = 0
print(patterns)
for x in range(len(designs)):
    print("add")
    score += check(x)
print("Score: ",score)
