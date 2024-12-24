import re

regA = 0
regB = 0
regC = 0
instructions = []
instPointer = 0


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
    global regA
    global regB
    global regC

    combo = comboVal(instructions[instPointer+1])
    print(combo&7,end=",")
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

parse("input1.txt")
print("RegA: ",regA,"\nRegB: ",regB,"\nRegC: ",regC,"\ninstruction codes: ",instructions)
while(instPointer < len(instructions)):
    eval(opDict[instructions[instPointer]])
print("\nRegA: ",regA,"\nRegB: ",regB,"\nRegC: ",regC,"\ninstruction codes: ",instructions)
