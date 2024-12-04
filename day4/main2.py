import re


def Rotate(a):
    output = ""
    inp = a.split("\n")
    if inp[len(inp)-1] == "":
        inp.pop()
    for x in range(len(inp[0])):
        for y in inp:
            output+=(y[x])
        output+="\n"
    return output
def rePosition(a,type):
    output =""
    iter =0
    inp = a.split("\n")
    if inp[len(inp)-1] == "":
        inp.pop()

    if type == 1:
        iter=0
    else:
        iter=len(inp)-1

    for x in inp:
        output += iter*" "
        output+=x
        output += ((len(inp)-1)-iter)*" "
        output+="\n"
        if type == 1:
            iter+=1
        else:
            iter-=1
    #print(output)
    return Rotate(output)

def cheack(input,x,y):
    req = ""
    q = r"MAS|SAM"
    inp = input.split("\n")
    for a in range(3):
        for b in range(3):
            req+=inp[x+b][y+a]
        req+="\n"

    #print(req) 
    if re.findall(q,rePosition(req,1)).__len__() != 0 and re.findall(q,rePosition(req,0)).__len__() != 0:
        return True
    return False

file = open("input.txt").read()
height = file.split("\n").__len__()-4
width = len(file.split("\n")[0])-3
sum =0
for x in range(width+1):
    for y in range(height+1):
        sum+=(cheack(file,x,y))
print("wynik: ",sum)
