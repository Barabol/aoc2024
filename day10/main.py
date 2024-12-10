coords = []
vals = []
zero = []
dimensions = [0,0]
score = 0
def add(x,y):
    global coords
    for z in coords:
        if z[0] == x and z[1] == y:
            return
    coords.append([x,y])
def parse():
    global zero
    global vals

    file = open("input.txt").read().split("\n")
    for x in range(len(file)):
        vals.append([])
        for y in file[x]:
            if y == '.':
                vals[x].append(-1)   
                continue
            if y=='0':
                zero.append([int(x),len(vals[x])])
            vals[x].append(int(y))

def isHykeable(x,y):
    global vals
    global score

    poss = [[1,0],[-1,0],[0,1],[0,-1]]
    for z in poss:
        if z[0]+x < dimensions[0] and z[1]+y < dimensions[1] and z[0]+x > -1 and z[1]+y > -1 and vals[x][y]-vals[x+z[0]][y+z[1]] == -1:
            if vals[x+z[0]][y+z[1]] == 9:
                add(x+z[0],y+z[1])
            else:
                isHykeable(x+z[0],y+z[1])

parse()
dimensions[1] = len(vals[0])
dimensions[0] = len(vals)-1
print(zero)
for x in zero:
    isHykeable(x[0],x[1])
    score += len(coords)
    coords = []
print("Score: ",score)

