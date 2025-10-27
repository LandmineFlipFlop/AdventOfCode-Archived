import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
# with open ('03_data/test_data', 'r') as casefile:
#     lines = casefile.read().splitlines()
with open ('03_data/p2_full_data', 'r') as casefile:
    lines = casefile.read().splitlines()
startTime = time.time()
count = 0

for line in lines:
    sides = line[1:len(line)].split(" ")
    i = 0
    while i < len(sides):
        sides[i] = int(sides[i])
        i += 1
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        count += 1


print(green("count: " + str(count)))
timerstop(startTime)