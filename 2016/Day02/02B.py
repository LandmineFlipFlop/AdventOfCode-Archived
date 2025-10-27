import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
# with open ('02_data/test_data', 'r') as casefile:
#     lines = casefile.read().splitlines()
with open ('02_data/full_data', 'r') as casefile:
    lines = casefile.read().splitlines()
startTime = time.time()
count = ""

x = 0
y = 2

keys = [["0","0","D","0","0"],["0","A","B","C","0"],["5","6","7","8","9"],["0","2","3","4","0"],["0","0","1","0","0"]]

for line in lines:
    for char in line:
        if char == "U":
            y += 1
            y = clamp(y,0,4)
            if keys[y][x] == "0":
                y += -1
        elif char == "D":
            y += -1
            y = clamp(y, 0, 4)
            if keys[y][x] == "0":
                y += 1
        elif char == "R":
            x += 1
            x = clamp(x, 0, 4)
            if keys[y][x] == "0":
                x += -1
        elif char == "L":
            x += -1
            x = clamp(x, 0, 4)
            if keys[y][x] == "0":
                x += 1
    count += keys[y][x]



print(green("count: " + str(count)))
timerstop(startTime)