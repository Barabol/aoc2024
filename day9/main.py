tabela =[]
def parse():
    global tabela
    file = open("input.txt").readline()[:-1]
    counter = 0
    for x in range(len(file)):
        for y in range(int(file[x])):
            if not x&1:
                tabela.append(counter)
            else:
                tabela.append(-1)
        if not x&1:
            counter+=1


def swap(x,y):
    global tabela
    if tabela[x] != -1:
        return True
    holder = tabela[x]
    tabela[x] = tabela[y]
    tabela[y] = holder
    return False

def format_():
    global tabela
    tabLen = len(tabela)
    index = tabLen-1

    for x in range(tabLen):
        if x == index:
            break
        if tabela[x] == -1:
            y=index
            while tabela[y] == -1:
                y-=1
            index = y
            if(index<x):
                break
            if swap(x,y) == True:
                break

def getVal():
    global tabela
    sum = 0
    for x in range(len(tabela)):
        if tabela[x] == -1:
            return sum
        sum+=tabela[x]*x
parse()
print(tabela)
format_()
print(tabela)
print(getVal())
