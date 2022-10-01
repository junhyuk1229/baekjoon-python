import sys
import math


def main():
    repeatNum = int(sys.stdin.readline().rstrip())
    numList = list(map(int, sys.stdin.readline().split(sep=" ")))
    totalNum = 0
    for checkNum in numList:
        if checkNum == 1:
            continue
        tempNum = 2
        while tempNum <= math.sqrt(checkNum):
            if checkNum % tempNum == 0:
                totalNum -= 1
                break
            tempNum += 1
        totalNum += 1
    print(totalNum)


if __name__ == "__main__":
    main()