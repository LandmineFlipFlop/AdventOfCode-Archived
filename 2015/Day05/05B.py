import sys, time, copy
sys.path.append("../../useful_functions.py")
from useful_functions import *
# with open ('05_data/test_data', 'r') as casefile:
#     lines = casefile.read().splitlines()
with open ('05_data/full_data', 'r') as casefile:
    lines = casefile.read().splitlines()
startTime = time.time()
count = 0

for line in lines:
    i = 0
    pair = False
    repeated = False
    while i < len(line):

        if i < len(line) - 1 and i != 0:
            if line[i] + line[i + 1] in line[0:i]:
                pair = True
                print('    ' + blue(line), yellow(line[i] + line[i + 1]))


        if i < len(line) - 2:
            if line[i] == line[i + 2]:
                repeated = True
                print('    ' + darkcyan(line), yellow(line[i] + line[i+1] + line[i+2]))

        i += 1

    if pair and repeated:
        count += 1
        print(green(line))
    else:
        print(red(line))


print(green("count: " + str(count)))
timerstop(startTime)