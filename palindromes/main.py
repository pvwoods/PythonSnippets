import sys
import os
from itertools import combinations

class PalindromeSetAnalyzer:
    
    def __init__(self, inputData):
        self.inputData = inputData.readlines()
        self.filters = []
        self.totalFilters = 1

    def analyze(self):
        result = []
        setPalindromes = []
        setBounds = []
        comboRange = []
        combinationSets = []
        palindromeMatches = []
        for case in self.inputData:
            # current upper and lower bounds for set
            setBounds = [int(n) for n in case.split()]
            # get all valid palindromes for the current set case
            setPalindromes = filter(lambda x: str(x) == str(x)[::-1], range(setBounds[0], setBounds[1] + 1))
            subSetMatches = 0
            comboRange = range(setBounds[0], setBounds[1] + 1)
            combinationSets = [[r, r] for r in comboRange]
            combinationSets += combinations(comboRange, 2)
            for subSet in combinationSets:
                # get a list of all the palindromes in the current subset
                palindromeMatches = set(range(subSet[0], subSet[1] + 1)) & set(setPalindromes)
                # apply any subset filters to check where the subset counts
                if(sum([f(palindromeMatches) for f in self.filters]) >= self.totalFilters):
                    subSetMatches += 1
            result.append(subSetMatches)
        return result

    def addSetFilter(self, f):
        self.filters.append(f)
        self.totalFilters = len(self.filters)

#############################################################

analyzer = PalindromeSetAnalyzer(open(sys.argv[1], "r"))
# any sets that do not have an even number of palindromes
# should be filtered out
analyzer.addSetFilter(lambda x: len(x) % 2 == 0)
print '\n'.join([str(r) for r in analyzer.analyze()])

