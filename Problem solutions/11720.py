import sys

lineLength = int(sys.stdin.readline().rstrip())
inputArr = sys.stdin.readline()
resultNum = 0

for indexNum in range(lineLength):
    resultNum += int(inputArr[indexNum])

print(resultNum)