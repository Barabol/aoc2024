file = open("./input.txt","r");
def getOp(numz,x,y):
    #numz = array("i",numz)
    if(int(numz[x]) == int(numz[y])):
       return 0
    elif(int(numz[x]) > int(numz[y])):
        return 1
    else:
        return 2

def isGut(numz,op):
    #print(numz)
    for y in range(len(numz)):
        if(y+1 == len(numz)):
            #print("x")
            return 1
        if getOp(numz,y,y+1) == 0 or getOp(numz,y,y+1) != op:
            return 0
        if  abs(int(numz[y]) - int(numz[y+1])) == 0 or  abs(int(numz[y]) - int(numz[y+1]))>3:
            #print(int(numz[y]) > int(numz[y+1]) != op , abs(int(numz[y]) - int(numz[y+1])) == 0 ,  abs(int(numz[y]) - int(numz[y+1]))>3)
            #print(numz[y],numz[y+1])
            return 0
    #print(" ")
    return 0
def ez(numz):
    op = getOp(numz,0,1)
    if(isGut(numz,op)):
       return 1
    for x in range(len(numz)):
        cp = numz.copy()
        cp.pop(x)
        op = getOp(cp,0,1)
        if(isGut(cp,op)):
           return 1
    return 0

nums = []
for line in file:
    nums.append(line.split(" "))

sum =0
for x in nums:    

    sum+=ez(x)
print("Wynik: ",sum)
