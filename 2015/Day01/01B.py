import sys, time, copy

sys.path.append("../../useful_functions.py")
from useful_functions import *
# with open ('01_data/test_data', 'r') as casefile:
#     line = casefile.read()
with open ('01_data/full_data', 'r') as casefile:
    line = casefile.read()

startTime = time.time()
count = 0

i=0
digitnum = 9999
while i < len(line):
    if line[i] == "(":
        count += 1
    else:
        count += -1

    if count < 0 and i < digitnum:
        digitnum = i
    i+= 1

print(green("count: " + str(digitnum + 1)))
timerstop(startTime)