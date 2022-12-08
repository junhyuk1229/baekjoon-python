import sys
import math


def checkSameLoc(oneX, oneY, twoX, twoY, pointX, pointY, radCir):
    distOne = math.sqrt(pow(oneX - pointX, 2) + pow(oneY - pointY, 2))
    distTwo = math.sqrt(pow(twoX - pointX, 2) + pow(twoY - pointY, 2))
    if (radCir < distOne and radCir < distTwo) or (radCir > distOne and radCir > distTwo):
        return 0
    return 1


def main():
    caseNum = int(sys.stdin.readline().rstrip())
    for i in range(caseNum):
        oneX, oneY, twoX, twoY = map(int, sys.stdin.readline().split(sep=' '))
        crossNum = 0
        cirNum = int(sys.stdin.readline().rstrip())
        for j in range(cirNum):
            pointX, pointY, radCir = map(int, sys.stdin.readline().split(sep=' '))
            if checkSameLoc(oneX, oneY, twoX, twoY, pointX, pointY, radCir) == 1:
                crossNum += 1
        print(crossNum)


if __name__ == "__main__":
    main()