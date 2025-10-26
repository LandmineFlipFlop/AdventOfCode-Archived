import sys, time, copy
sys.path.append("../../useful_functions.py")
from useful_functions import *
# with open ('03_data/test_data', 'r') as casefile:
#     line = casefile.read()
with open ('03_data/full_data', 'r') as casefile:
    line = casefile.read()
startTime = time.time()

houses = {(0,0):1}

x = 0
y = 0

i=0
while i < len(line):
    if line[i] == '^':
        y += 1
    elif line[i] == 'v':
        y += -1
    elif line[i] == '>':
        x += 1
    elif line[i] == '<':
        x += -1
    if (y,x) in houses:
        houses[(y, x)] += 1
    else:
        houses[(y, x)] = 1

    i += 1

print(green("count: " + str(len(houses))))
timerstop(startTime)