import re

input = [[]]
freebee = True

def read():
    global input
    file = open("input.txt","r")
    counter =0
    for line in file:
        for x in line.split(" "):
            input[counter].append(int(re.findall(r"\d+",x)[0]))
        counter+=1
        input.append([])
    input.pop()
    print(input)

def opr(numbers,index,op):
    val = op[0]
    op.pop(0)
    #val = val >> index
    #print(val)
    #print(val,numbers)
    used = numbers[1]
    numbers.pop(1)
    if val == 0:
        numbers[0] = numbers[0]+used
        return
    else:
        numbers[0] = numbers[0]*used
        return

def addBinarly(op):
    global freebee
    
    if freebee == True:
        freebee = False
        return False

    added=False


    for x in  range(len(op)):
        if not added:
            if op[x] == 0:
                op[x] = 1
                added = True
                return False

            elif op[x] == 1:
                op[x] = 0
    return True
def combinations(index):
    global freebee

    #symbols = ["\033[31;1m\033[0m","\033[92;1m\033[0m"]

    freebee = True
    ifTrue = 0

    eq = input[index][0]
    numbers = input[index][1:]
    score = 0
    op = [0]*(len(numbers)-1)
    #print("\n",numbers,"\n")

    while addBinarly(op) != True:
        temp = numbers.copy()
        opCpy = op.copy()

        for y in range(len(numbers)-1):
            opr(temp,y,opCpy)
        if ifTrue == 0:
            ifTrue=temp[0]
        if temp[0] == eq:
            return eq

        #print(symbols[int(eq==temp[0])],op,eq,temp)

        count = len(op)

        for z in  range(len(op)):
            if op[z] == 1:
                count-=1

        if count == 0:
            break

    return score

read()
score =0
for x in range(len(input)):
    score += combinations(x)
print(combinations(1))
print("Score: ",score)
