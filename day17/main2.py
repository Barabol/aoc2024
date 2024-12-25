import re
import time

regA = 0
regB = 0
regC = 0
instructions = []
instPointer = 0

initRegA = 1
output = []
added = False


def parse(fileName):
    global regA
    global regB
    global regC
    global instructions

    file = open(fileName,"r").read().split("\n")
    regA = int(re.findall(r"\d+",file[0])[0])
    regB = int(re.findall(r"\d+",file[1])[0])
    regC = int(re.findall(r"\d+",file[2])[0])

    for x in re.findall(r"\d+",file[4]):
        instructions.append(int(x))
def comboVal(x):
    match x:
        case 4:
            return regA
        case 5:
            return regB
        case 6:
            return regC
    return x

def adv():
    global instructions
    global instPointer
    global regA
    global regB
    global regC

    combo = comboVal(instructions[instPointer+1])
    regA = regA // (2**combo)
    instPointer+=2

def bxl():
    global instructions
    global instPointer
    global regB

    literalV = instructions[instPointer+1]
    regB ^= literalV
    instPointer+=2

def bst():
    global instructions
    global instPointer
    global regA
    global regB
    global regC

    combo = comboVal(instructions[instPointer+1])
    regB = combo&7
    instPointer+=2

def jnz():
    global instructions
    global instPointer
    global regA
    global regB
    global regC

    literalV = instructions[instPointer+1]
    instPointer+=2
    if regA == 0:
        return
    instPointer = literalV


def bxc():
    global instructions
    global instPointer
    global regA
    global regB
    global regC
    regB = regB ^ regC
    instPointer+=2

def out():
    global instructions
    global instPointer
    global output
    global added
    global regA
    global regB
    global regC

    combo = comboVal(instructions[instPointer+1])
    output.append(combo&7)
    added = True

    instPointer+=2

def bdv():
    global instructions
    global instPointer
    global regA
    global regB
    global regC

    combo = comboVal(instructions[instPointer+1])
    regB = regA // (2**combo)
    instPointer+=2

def cdv():
    global instructions
    global instPointer
    global regA
    global regB
    global regC

    combo = comboVal(instructions[instPointer+1])
    regC = regA // (2**combo)
    instPointer+=2

opDict={
    0:"adv()",
    1:"bxl()",
    2:"bst()",
    3:"jnz()",
    4:"bxc()",
    5:"out()",
    6:"bdv()",
    7:"cdv()"
}
def emulate():
    while(instPointer < len(instructions)):
        eval(opDict[instructions[instPointer]])

def emulatePP():
    global added
    global regA
    global regB
    global regC
    global output
    global initRegA
    global instructions
    global instPointer
    output = []
    regA = initRegA
    regB = 0
    regC = 0
    added = False
    instPointer = 0
    #print("RegA: ",regA,"\nRegB: ",regB,"\nRegC: ",regC,"\ninstruction codes: ",instructions)
    while(instPointer < len(instructions)):

        print(instructions[instPointer],instructions[instPointer+1])
        eval(opDict[instructions[instPointer]])
        
        if added:
            for x in range(len(output)):
                if output[x] != instructions[x]:
                    return False
            added = False
    if len(output) != len(instructions):
       return False
    print("> ",initRegA)
    return True

parse("input1.txt")
initRegA = 1
#print(emulatePP())
#print(output)
a = time.time()
while emulatePP() == False:
    print("next ",initRegA)
    initRegA+=1
print("Wydajność? ",time.time() - a)

