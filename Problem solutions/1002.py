import sys
import math


def intersectCheck(xOne, yOne, radOne, xTwo, yTwo, radTwo):
    distPoints = math.sqrt(math.pow(xOne - xTwo, 2) + math.pow(yOne - yTwo, 2))
    if radOne + radTwo < distPoints:
        return 0
    if radOne + radTwo == distPoints:
        return 1
    if abs(radOne - radTwo) < distPoints < radOne + radTwo:
        return 2
    if abs(radOne - radTwo) == distPoints and distPoints != 0:
        return 1
    if 0 < distPoints < abs(radOne - radTwo):
        return 0
    if radOne == radTwo:
        return -1
    return 0


def main():
    testNum = int(sys.stdin.readline().rstrip())
    for i in range(testNum):
        xOne, yOne, radOne, xTwo, yTwo, radTwo = map(int, sys.stdin.readline().split(sep=' '))
        outputNum = intersectCheck(xOne, yOne, radOne, xTwo, yTwo, radTwo)
        print(outputNum)


if __name__ == "__main__":
    main()