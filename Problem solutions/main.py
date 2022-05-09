import sys

inputCount = int(sys.stdin.readline().rstrip())

for count in range(inputCount):
    inputStr = sys.stdin.readline().rstrip()
    checkArr = []
    for _ in range(26):
        checkArr.append(0)

