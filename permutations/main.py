import sys
import os
from itertools import permutations

class PermutationAnalyzer:
    
    def __init__(self, inputData):
        self.inputData = inputData.readlines()

    def analyze(self):
        result = []
        permutationSet = []
        for case in self.inputData:
            permutationSet = permutations(list(case.rstrip()))
            result.append(','.join(sorted([''.join(p) for p in list(permutationSet)])))
        return result

#############################################################

analyzer = PermutationAnalyzer(open(sys.argv[1], "r"))
print '\n'.join([str(r) for r in analyzer.analyze()])

