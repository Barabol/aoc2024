file = []
lookupTable = []
limit = 25

def parse():
    global file
    file = open("input.txt","r").read().split("\n")[0].split(" ")

def render(a):
    tab = []
    tab.append(a)
    global limit
    for y in range(limit):
        sizer = len(tab)
        for x in range(sizer):
            if tab[x] == '0':
                tab[x] = '1'
                continue

            if len(tab[x]) & 1:#nie parzyste
                tab[x] = str(int(tab[x])*2024)
                continue
            
            else:#pażyste
                tabStr = (tab[x])
                #print(tab[x])
                tab.append(str(int(tabStr[len(tabStr)//2:])))
                tab[x] = (tabStr[:-len(tabStr)//2])
                #print(tab[x])
                #print(tab[len(tab)-1])
                continue
    
    #print(a,tab)
    return len(tab)
    
parse()
#print(file)
score=0

for x in file:
    score += render(x)
print(score)

