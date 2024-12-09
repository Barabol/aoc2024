tabela =[]
def parse():
    global tabela
    file = open("input.txt").readline()[:-1]
    counter = 0
    for x in range(len(file)):
        if not x&1:
            tabela.append([counter,int(file[x])])
        else:
            tabela.append([-1,int(file[x])])
        if not x&1:
            counter+=1


def swap(x,y):
    global tabela
    if(tabela[x][1] == tabela[y][1]):
        holder = tabela[x][0]
        tabela[x][0] = tabela[y][0]
        tabela[y][0] = holder
        return False
    else:
        # x górny index
        # y dolny index (aka -1)
        holder = tabela[y][1] - tabela[x][1]
        tabela[y][1]=tabela[x][1]
        tabela.insert(y+1,[-1,int(holder)])
        swap(x+1,y)

        return False
def format_():
    global tabela
    tabLen = len(tabela)
    index = tabLen-1

    for x in range(tabLen):
        if tabela[index - x][0] != -1:
            for y in range(index - x):
                if tabela[y][0] == -1 and tabela[y][1] >= tabela[index - x][1]:
                    swap(index - x,y)
                    break

def getVal():
    global tabela
    tab = []
    for x in tabela:
        for y in range(x[1]):
            tab.append(x[0])
    sum = 0
    for x in range(len(tab)):
        if tab[x] == -1:
            continue
        sum+=tab[x]*x
    return sum
parse()
format_()
print(getVal())
