import sys


def checkCondition(inputNum):
    if inputNum < 100:
        return 1
    else:
        ratio = ((inputNum // 10) % 10) - (inputNum % 10)
        inputNum //= 10
        while inputNum >= 10:
            if ratio != ((inputNum // 10) % 10) - (inputNum % 10):
                return 0
            inputNum //= 10
        return 1


inputNum = int(sys.stdin.readline().rstrip())
resultCount = 0

for i in range(1, inputNum + 1):
    if checkCondition(i) == 1:
        resultCount += 1

print(resultCount)