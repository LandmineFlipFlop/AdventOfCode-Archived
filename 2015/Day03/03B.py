import sys, time, copy
sys.path.append("../../useful_functions.py")
from useful_functions import *
# with open ('03_data/test_data', 'r') as casefile:
#     line = casefile.read()
with open ('03_data/full_data', 'r') as casefile:
    line = casefile.read()
startTime = time.time()

houses = {(0,0):1}

sx = 0
sy = 0
bx = 0
by = 0

i=0
while i < len(line):
    if line[i] == '^':
        sy += 1
    elif line[i] == 'v':
        sy += -1
    elif line[i] == '>':
        sx += 1
    elif line[i] == '<':
        sx += -1
    if (sy, sx) in houses:
        houses[(sy, sx)] += 1
    else:
        houses[(sy, sx)] = 1
    i += 1

    if line[i] == '^':
        by += 1
    elif line[i] == 'v':
        by += -1
    elif line[i] == '>':
        bx += 1
    elif line[i] == '<':
        bx += -1
    if (by, bx) in houses:
        houses[(by, bx)] += 1
    else:
        houses[(by, bx)] = 1
    i += 1

print(green("count: " + str(len(houses))))
timerstop(startTime)