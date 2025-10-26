import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
# with open ('01_data/test_data', 'r') as casefile:
#     lines = casefile.read()
with open ('01_data/full_data', 'r') as casefile:
    lines = casefile.read()
startTime = time.time()
count = 0

actions = lines.split(", ")

rot = 0
x = 0
y = 0

for action in actions:
    if action[0] == "R":
        rot += 1
    else:
        rot += -1
    rot = rot%4

    if rot == 0:
        y += int( action[1:len(action)] )
    elif rot == 2:
        y -= int(action[1:len(action)])
    elif rot == 1:
        x += int(action[1:len(action)])
    else:
        x -= int(action[1:len(action)])
    print(blue(rot), yellow( str(x)+","+str(y)) )
count = abs(x) + abs(y)

print(green("count: " + str(count)))
timerstop(startTime)