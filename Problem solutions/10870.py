import sys


def phibo(inputNum):
    if inputNum == 0:
        return 0
    if inputNum == 1:
        return 1
    return phibo(inputNum - 2) + phibo(inputNum - 1)


def main():
    inputNum = int(sys.stdin.readline().rstrip())

    resultNum = phibo(inputNum)

    print(resultNum)


if __name__ == "__main__":
    main()