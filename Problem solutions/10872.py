import sys


def fact(inputNum):
    if inputNum <= 1:
        return 1
    else:
        return fact(inputNum - 1) * inputNum


def main():
    inputNum = int(sys.stdin.readline().rstrip())

    resultNum = fact(inputNum)

    print(resultNum)

if __name__ == "__main__":
    main()