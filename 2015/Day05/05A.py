import sys, time, copy
sys.path.append("../../useful_functions.py")
from useful_functions import *
# with open ('05_data/test_data', 'r') as casefile:
#     lines = casefile.read().splitlines()
with open ('05_data/full_data', 'r') as casefile:
    lines = casefile.read().splitlines()
startTime = time.time()
count = 0

# print(green(lines))

for line in lines:
    # print(blue(line))
    if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
        pass
    else:
        i = 0
        vowels = 0
        pair = False
        while i < len(line):
            if line[i] == 'a' or line[i] == 'e' or line[i] == 'i' or line[i] == 'o' or line[i] == 'u':
                vowels += 1

            if i >= 1:
                if line[i] == line[i - 1]:
                    pair = True

            i += 1

        if vowels >= 3 and pair:
            count += 1
        # else:
        #     if not pair:
        #         print(yellow("no pair ") + red(line))
        #     if vowels < 3:
        #         print(yellow("not enough vowels ") + red(line))



print(green("count: " + str(count)))
timerstop(startTime)