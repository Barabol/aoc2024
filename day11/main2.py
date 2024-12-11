import time
file = []
lookupTable = []
limit = 75  

def parse():
    global file
    file = open("input.txt","r").read().split("\n")[0].split(" ")

def render(a):
    tab = []
    tab.append([a,1])
    global limit
    for y in range(limit):
        sizer = len(tab)
        for x in range(sizer):
            #print(tab[x])
            if tab[x][0] == '0':
                tab[x][0] = '1'
                continue

            if len(tab[x][0]) & 1:#nie parzyste
                tab[x][0] = str(int(tab[x][0])*2024)
                continue
            
            else:#pażyste
                tabStr = (tab[x][0])
                #print("he",tab[x])
                tab.append([str(int(tabStr[len(tabStr)//2:])),tab[x][1]])
                tab[x][0] = (tabStr[:-len(tabStr)//2])
                #print(tab[x])
                #print(tab[len(tab)-1])
                continue

        tab2 = []
        for z in range(len(tab)):
            appended= False
            for v in range(len(tab2)):
                if(tab2[v][0] == tab[z][0]):
                    tab2[v][1] += tab[z][1]
                    appended = True
                    break
            if not appended:
                tab2.append(tab[z])
        tab = tab2
        #print("\n",tab2,"\n")

    print(a,tab)
    scr = 0
    for x in tab:
        scr+=x[1]
    return scr
    
parse()
#print(file)
score=0
a = time.time()
for x in file:
    score += render(x)
print(score,time.time()-a)

