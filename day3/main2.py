import re
file = open("./input.txt")
input = file.read()
input2 = input.split("don't()")

#print(ret)
used = ""
used+=input2[0]
for x in input2:
    #input2[x].split("do()")
    z = x.split("do()")
    for y in range(len(z)):
        if y!= 0:
            used+=z[y]
ret = re.findall(r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)",used)
val =0
for x in ret:
    gg1 = re.findall("[0-9][0-9]?[0-9]?,",x)
    gg2 = re.findall(",[0-9][0-9]?[0-9]?",x)
    gg1 = re.findall("[0-9][0-9]?[0-9]?",gg1[0])
    gg2 = re.findall("[0-9][0-9]?[0-9]?",gg2[0])
    val += int(gg1[0])*int(gg2[0])
print(val)
