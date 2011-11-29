import sys
import os

class PolishNotationCalculator:

    def __init__(self, inputData):
        self.inputData = inputData.readlines()
        self.operatorFilter = lambda x: x in '*/+'
        self.operatorTable = {
                                '*' : lambda x, y: x * y,
                                '/' : lambda x, y: x / y if y != 0 else 0,
                                '+' : lambda x, y: x + y
        }

    def analyze(self):
        result = []
        operations = []
        operands = []
        currentCase = []
        caseValue = 0
        operationStep = 0
        for case in self.inputData:
            currentCase = case.rstrip().split(' ')
            operations = filter(self.operatorFilter, currentCase)
            operands = [int(a) for a in currentCase if a not in operations]
            # there should always be 1 more operand then operation
            if len(operations) + 1 == len(operands):
                caseValue = operands[0]
                operationStep = 0
                for operation in reversed(operations):
                    operationStep += 1
                    caseValue = self.operatorTable[operation](caseValue, operands[operationStep])
                result.append(caseValue)
            else:
                print "Error :: Operand / Operation length mismatch"
        return result


#############################################################

analyzer = PolishNotationCalculator(open(sys.argv[1], "r"))
print '\n'.join([str(r) for r in analyzer.analyze()])
