from copy import deepcopy
from typing import Final
import re


#+---+---+---+
#| 7 | 8 | 9 |
#+---+---+---+
#| 4 | 5 | 6 |
#+---+---+---+
#| 1 | 2 | 3 |
#+---+---+---+
#    | 0 | A |
#    +---+---+

#    +---+---+
#    | ^ | A |
#+---+---+---+
#| < | v | > |
#+---+---+---+

arrowDict : Final= {          "^":[1,0],"A":[2,0],
             "<":[0,1],"v":[1,1],">":[2,1]}

arrowStartPoz : Final = arrowDict["A"]

buttonDict : Final={"7":[0,0],"8":[1,0],"9":[2,0],
            "4":[0,1],"5":[1,1],"6":[2,1],
            "1":[0,2],"2":[1,2],"3":[2,2],
                      "0":[1,3],"A":[2,3]}
startPoz :Final = buttonDict["A"]

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
ACTION = 4

dirs=[[0,0],[0,0],[0,0],[0,0]]
dirs[UP] = [0,-1]
dirs[DOWN] = [0,1]
dirs[LEFT] = [-1,0]
dirs[RIGHT] = [1,0]

dirNames = {UP:"^",DOWN:"v",LEFT:"<",RIGHT:">",ACTION:"A"}

buttons = []
def parse(fileName):
    file = open(fileName,"r")
    for x in file:
        buttons.append(re.findall(r"\d",x))
        buttons[len(buttons)-1].append("A")
        buttons[len(buttons)-1].append(int(re.findall(r"\d+",x)[0]))

def reParse(toDo,len):
    string=""
    index = 0
    next = toDo[index]
    now = deepcopy(arrowStartPoz)
    print("\n",toDo,len,toDo[index])
    print(now,arrowDict)
    #print("now: ",now,"going to: ",arrowDict[toDo[index]])

    while True:
        #print(now,arrowDict[next])

        if now[1] != arrowDict[next][1]:
            if (now[1]-arrowDict[next][1]) >= (now[0]-arrowDict[next][0]):
                if now[0] > arrowDict[next][0]:
                    now[0]-=1
                    #print("<")
                    string+="<"
                    continue

                if now[0] < arrowDict[next][0]:
                    now[0]+=1
                    #print(">")
                    string+=">"
                    continue
        else:
            if now[0] > arrowDict[next][0]:
                now[0]-=1
                #print("<")
                string+="<"
                continue

            if now[0] < arrowDict[next][0]:
                now[0]+=1
                #print(">")
                string+=">"
                continue
        if now[0] != arrowDict[next][0]:
            if (now[0]-arrowDict[next][0]) >= (now[1]-arrowDict[next][1]):
                if now[1] < arrowDict[next][1]:
                    now[1]+=1
                    #print("v")
                    string+="v"
                    continue

                if now[1] > arrowDict[next][1]:
                    now[1]-=1
                    #print("^")
                    string+="^"
                    continue
        else:
            if now[1] < arrowDict[next][1]:
                now[1]+=1
                #print("v")
                string+="v"
                continue

            if now[1] > arrowDict[next][1]:
                now[1]-=1
                #print("^")
                string+="^"
                continue
       
        if now[1] == arrowDict[next][1] and now[0] == arrowDict[next][0]:
            index+=1
            string+="A"
            if index>=len:
                break
            #print("now: ",now,"going to: ",arrowDict[toDo[index]])
            next = toDo[index]
    return [string,string.__len__()]
def process(toDo):
    print(toDo)
    string = ""
    used = toDo[0]
    index = 0
    now = deepcopy(startPoz)
    while type(used) != int:
        if now[0] > buttonDict[used][0]:
            now[0]-=1
            string+="<"
            continue

        if now[0] < buttonDict[used][0]:
            now[0]+=1
            string+=">"
            continue

        if now[1] > buttonDict[used][1]:
            now[1]-=1
            string+="^"
            continue

        if now[1] < buttonDict[used][1]:
            now[1]+=1
            string+="v"
            continue

        if now[0] == buttonDict[used][0] and now[1] == buttonDict[used][1]:
            string+="A"
            index+=1
            used = toDo[index]
    parsed = reParse(string,len(string))
    parsed  = reParse(parsed[0],parsed[1])
    print(parsed[1],used,parsed[0])
    return parsed[1]*used
parse("input1.txt")
print(buttons)
score = 0
#for x in buttons:
#    score += process(x)
score += process(buttons[2])
print("score: ",score)
