import sys, time, copy
sys.path.append("../../useful_functions.py")
from useful_functions import *
# with open ('06_data/test_data', 'r') as casefile:
#     lines = casefile.read().splitlines()
with open ('06_data/full_data', 'r') as casefile:
    lines = casefile.read().splitlines()
startTime = time.time()
count = 0

grid=[]
size = 1000

i = 0
while i < size:
    i2 = 0
    grid.append([])
    while i2 < size:
        grid[i].append(0)
        i2 += 1
    i += 1

# printmap(grid)


for line in lines:
    coords = line[1:len(line)].split(',')

    i = 0
    while i < len(coords):
        coords[i] = int(coords[i])
        i += 1

    if line[0] == 'f':

        i = coords[0]
        while i <= coords[2]:
            i2 = coords[1]
            while i2 <= coords[3]:
                if grid[i][i2] > 0:
                    grid[i][i2] += -1
                i2 += 1
            i += 1

        print(blue('f'), )
    elif line[0] == 'n':

        i = coords[0]
        while i <= coords[2]:
            i2 = coords[1]
            while i2 <= coords[3]:
                grid[i][i2] += 1
                i2 += 1
            i += 1

        print(yellow('n'))
    elif line[0] == 't':

        i = coords[0]
        while i <= coords[2]:
            i2 = coords[1]
            while i2 <= coords[3]:
                grid[i][i2] += 2
                i2 += 1
            i += 1

        print(purple('t'))
    i = 0

i = 0
while i < size:
    i2 = 0
    while i2 < size:
        count += grid[i][i2]
        i2 += 1
    i += 1

# printmap(grid)

print(  green("count: " + str(count) )  )
timerstop(startTime)