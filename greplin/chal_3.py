from itertools import *

testSet = [3, 4, 9, 14, 15, 19, 28, 37, 47, 50, 54, 56, 59, 61, 70, 73, 78, 81, 92, 95, 97, 99]
subsets = 0

for x in range(1, (len(testSet) - 1)):
    for i in combinations(testSet, x):
        if (sum(i) - i[-1]) == i[-1]:
            print i
            subsets += 1
                
print subsets
