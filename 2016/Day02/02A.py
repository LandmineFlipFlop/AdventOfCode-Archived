import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
# with open ('02_data/test_data', 'r') as casefile:
#     lines = casefile.read().splitlines()
with open ('02_data/full_data', 'r') as casefile:
    lines = casefile.read().splitlines()
startTime = time.time()
count = ""

x = 1
y = 1

keys = [[7,8,9],[4,5,6],[1,2,3]]

for line in lines:
    for char in line:
        if char == "U":
            y += 1
            y = clamp(y,0,2)
            # print(blue(y))
        elif char == "D":
            y += -1
            y = clamp(y, 0, 2)
            # print(blue(y))
        elif char == "R":
            x += 1
            x = clamp(x, 0, 2)
            # print(green(x))
        elif char == "L":
            x += -1
            x = clamp(x, 0, 2)
            # print(green(x))
    count += str(keys[y][x])



print(green("count: " + str(count)))
timerstop(startTime)