import sys
import math


def main():
    firstNum = int(sys.stdin.readline().rstrip())
    lastNum = int(sys.stdin.readline().rstrip())
    sumNum = 0
    firstPrime = 0
    while firstNum <= lastNum:
        if firstNum == 1:
            firstNum += 1
            continue
        tempNum = 2
        while tempNum <= math.sqrt(firstNum):
            if firstNum % tempNum == 0:
                sumNum -= firstNum
                break
            tempNum += 1
        sumNum += firstNum
        if firstPrime == 0:
            firstPrime = sumNum
        firstNum += 1
    if firstPrime == 0:
        print(-1)
    else:
        print(sumNum)
        print(firstPrime)

if __name__ == "__main__":
    main()