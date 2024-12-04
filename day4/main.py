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
file = open("input.txt").read()
ret = re.findall(r"XMAS|SAMX",file)
amm =0

print("----------------")

print("Horyzontalne XMAS: ",re.findall(r"XMAS",file).__len__())
amm +=re.findall(r"XMAS",file).__len__()
print("Horyzontalne SAMX: ",re.findall(r"SAMX",file).__len__())
amm +=re.findall(r"SAMX",file).__len__()

print("----------------")

print("Wertykalne XMAS: ",re.findall(r"XMAS",Rotate(file)).__len__())
amm+=re.findall(r"XMAS",Rotate(file)).__len__()
print("Wertykalne SAMX: ",re.findall(r"SAMX",Rotate(file)).__len__())
amm+=re.findall(r"SAMX",Rotate(file)).__len__()

print("----------------")

print("Wertykalne XMAS: ",re.findall(r"XMAS",rePosition(file,0)).__len__())
amm+=re.findall(r"XMAS",rePosition(file,0)).__len__()
print("Wertykalne SAMX: ",re.findall(r"SAMX",rePosition(file,0)).__len__())
amm+=re.findall(r"SAMX",rePosition(file,0)).__len__()

print("----------------")

print("Wertykalne XMAS: ",re.findall(r"XMAS",rePosition(file,1)).__len__())
amm+=re.findall(r"XMAS",rePosition(file,1)).__len__()
print("Wertykalne SAMX: ",re.findall(r"SAMX",rePosition(file,1)).__len__())
amm+=re.findall(r"SAMX",rePosition(file,1)).__len__()

print("----------------")
print("Wynik: ",amm)
