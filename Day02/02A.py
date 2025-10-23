import sys, time, copy
sys.path.append("../useful_functions.py")
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
    sides = [(int(temp[0]) * int(temp[1])), (int(temp[0]) * int(temp[2])), (int(temp[1]) * int(temp[2]))]
    count += sum(sides) * 2
    sides.sort()
    count += sides[0]

print(green("count: " + str(count)))
timerstop(startTime)