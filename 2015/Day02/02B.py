import sys, time, copy
sys.path.append("../../useful_functions.py")
from useful_functions import *
# with open ('02_data/test_data', 'r') as casefile:
#     lines = casefile.read().splitlines()
with open ('02_data/full_data', 'r') as casefile:
    lines = casefile.read().splitlines()
startTime = time.time()
count = 0

temp = []

for item in lines:
    temp = item.split('x')
    sides = [2*int(temp[0]) + 2*int(temp[1]), 2*int(temp[0]) + 2*int(temp[2]), 2*int(temp[1]) + 2*int(temp[2])]
    sides.sort()
    print(sides)
    count += sides[0]
    count += int(temp[0]) * int(temp[1]) * int(temp[2])

print(green("count: " + str(count)))
timerstop(startTime)