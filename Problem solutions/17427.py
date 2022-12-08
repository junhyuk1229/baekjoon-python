import sys


def main():
    inputNum = int(sys.stdin.readline().rstrip())
    tempNum = 1
    sumNum = 0
    while tempNum <= inputNum:
        sumNum += (inputNum // tempNum) * tempNum
        tempNum += 1
    print(sumNum)


if __name__ == "__main__":
    main()