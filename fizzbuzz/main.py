import sys

class FizzBuzzer:

    def __init__(self, inputData):
        self.inputData = inputData.readlines()

    def execute(self):
        for case in self.inputData:
            result = ''
            data = [int(n) for n in case.split()]
            for i in range(1, data[2] + 1):
                tmp = ''
                tmp += 'Fizz' if (i % data[0] == 0) else ''
                tmp += 'Buzz' if (i % data[1] == 0) else ''
                result += (tmp if (tmp != '') else str(i)) + ','
            print result

analyzer = FizzBuzzer(open(sys.argv[1], "r"))
analyzer.execute()
