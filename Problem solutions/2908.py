import sys


def changeInt(inputInt):
    tempInt = 0
    while inputInt > 0:
        tempInt *= 10
        tempInt += inputInt % 10
        inputInt //= 10
    return tempInt


firstNum, secondNum = map(int, sys.stdin.readline().split())
if changeInt(firstNum) > changeInt(secondNum):
    print(changeInt(firstNum))
else:
    print(changeInt(secondNum))