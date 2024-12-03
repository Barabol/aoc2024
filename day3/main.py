import re
file = open("./input.txt")
input = file.read()
input2 = input.split("don't()")
print(input2.__len__())
ret = re.findall("mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)",input)
val =0
for x in ret:
    gg1 = re.findall("[0-9][0-9]?[0-9]?,",x)
    gg2 = re.findall(",[0-9][0-9]?[0-9]?",x)
    gg1 = re.findall("[0-9][0-9]?[0-9]?",gg1[0])
    gg2 = re.findall("[0-9][0-9]?[0-9]?",gg2[0])
    val += int(gg1[0])*int(gg2[0])
print(val)
