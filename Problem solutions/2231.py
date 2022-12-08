import sys


def checkDiv(inputNum):
    tempTens = 1
    checkNum = inputNum

    while tempTens < inputNum:
        checkNum -= 9
        tempTens *= 10

    if checkNum < 0:
        checkNum = 1

    while checkNum != inputNum:
        tempNum = checkNum
        tempTens = 1
        while tempTens < checkNum:
            tempNum += (checkNum // tempTens) % 10
            tempTens *= 10
        if tempNum == inputNum:
            break
        checkNum += 1

    if checkNum == inputNum:
        print(0)
    else:
        print(checkNum)


def main():
    inputNum = int(sys.stdin.readline().rstrip())
    checkDiv(inputNum)


if __name__ == "__main__":
    main()