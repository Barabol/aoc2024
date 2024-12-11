retw = []
updates=[]
def isIn(a):
    if retw.__len__() == 0:
       return -1
    count = -1
    for x in retw:
        count+=1
        if x[0] == a:
            return count
    return -1
def red():
    c = 0
    for line in file:
        if line == "\n":
            c+=1
        match(c):
            case 0:
                splitter = [int(line.split("|")[0]),int(line.split("|")[1][:-1])]
                holder = isIn(splitter[0])
                if holder == -1:
                    retw.append(splitter)
                else:
                    retw[holder].append(splitter[1])
            case 1:
                c+=1
            case 2:
                index = updates.__len__();
                updates.append([])
                for x in line[:-1].split(","):
                    updates[index].append(int(x))

def indexOf(lista,a):
    for x in range(len(lista)):
        if lista[x] == a:
            return x
    return -1
def check(lista,index):
    holder = retw[isIn(lista[index])]
    #print("\n",lista)
    #print(holder,lista[index])
    for l in range(len(lista)):
        #print(indexOf(holder,lista[l]),lista[l])
        if indexOf(holder,lista[l]) > 0 and lista[l] != lista[index] and indexOf(lista,lista[l]) < index:
            #print(lista,index,l)
            return False
    return True 
def isGut(a):
    kek = True
    for y in range(len(a)):
        if kek==True and isIn(a[y]) != -1:
            #print(y)
            if check(a,y)==False:
                kek = False
    return kek
def format_(lista):
    print()
file = open("input.txt","r")
red()
gut = []
kek = False
for x in updates:
    if isGut(x) == True:
        gut.append(x)
print("\n",gut)
format_(gut)
sum=0
for x in gut:
    sum+=(x[(len(x)//2)])
print("wynik: ",sum)
