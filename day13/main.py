
import re

cost = [3,1]
nums = []

def parse():
    global nums
    state = 0
    holder = [[],[],[]]
    for x in open("input.txt","r").read().split("\n"):
        if len(x)<3:
            continue
        for z in re.findall(r"\d+",x):
            #print(int(z),end=" ")
            holder[state].append(int(z))

        if state == 2:
            state = 0
            #print(holder)
            nums.append(holder.copy())
            holder = [[],[],[]]
        else:
            state += 1

def getValuez(tab):
    global cost
    buttonA = tab[0].copy()
    buttonB = tab[1].copy()
    needed = tab[2].copy()
    xHolder = 0
    yHolder = 0

    #buttonA = [2,1]
    #buttonB = [1,2]
    #needed = [8,10]
    
    buttonB[1]*=buttonA[0]
    needed[1]*=buttonA[0]

    buttonB[1]-=buttonA[1]*buttonB[0]
    needed[1]-=buttonA[1]*needed[0]

    yHolder = needed[1]//buttonB[1]

    xHolder = (needed[0]-(needed[1]//buttonB[1])*buttonB[0])//buttonA[0]

    #print(tab[0][0],"x+",tab[1][0],"y =",tab[2][0],";",tab[0][1],"x+",tab[1][1],"y =",tab[2][1])
    #print("x = ",xHolder,"\ny = ",yHolder)
    if xHolder*tab[0][0]+yHolder*tab[1][0] != tab[2][0] or xHolder*tab[0][1]+yHolder*tab[1][1] != tab[2][1]:
        #print("F")
        return []
    return [[xHolder,yHolder]]


def run():
    score = 0
    for x in nums:
        hold = getValuez(x)

        if(len(hold)>1):
            print(hold)
        if(len(hold) == 1):
            #print("A")
            score+=(hold[0][0]*3)+hold[0][1]
    print(score)

print("----------------------------")
parse()
run()
#print(getValuez(nums[0]))
