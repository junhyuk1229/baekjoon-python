import sys


def main():
    firstNum, secondNum = map(int, sys.stdin.readline().split(sep=' '))
    commonFactor = firstNum
    if commonFactor > secondNum:
        commonFactor = secondNum
    while True:
        if firstNum % commonFactor == 0 and secondNum % commonFactor == 0:
            break
        commonFactor -= 1
    print(commonFactor)
    print(firstNum * secondNum // commonFactor)


if __name__ == "__main__":
    main()