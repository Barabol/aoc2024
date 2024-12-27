keys = []
locks = []

def parse(fileName):
    global keys
    global locks

    file = open(fileName,"r").read().split("\n")

    test = "#"*(len(file[0]))

    used = [-1]*len(file[0])

    offset = 1
    isKey = False

    for y in range(len(file)):
        
        if file[y] == "":
            #print(used)

            if isKey == True:
                keys.append(used)

            else: 
                locks.append(used)

            used = [-1]*len(file[0])
            offset=0
            isKey = False

        if offset == 1 and test == file[y]:
            isKey = True

        for x in range(len(file[y])):
            if file[y][x] == "#":
                used[x]+=1

        offset += 1
def getScore():
    global locks
    global keys

    score = 0
    gut = True
    for x in range(len(locks)):
        for y in range(len(keys)):
            gut = True
            for z in range(len(locks[x])):
                if locks[x][z] + keys[y][z] > 5:
                    gut = False
                    break
            if gut == True:
                score+=1
            

    return score

parse("./input.txt")
print("Keys: ",keys)
print("Locks: ",locks)
print("Score: ",getScore())
