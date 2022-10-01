import sys


def main():
    firstNum, secondNum = map(int, sys.stdin.readline().split(sep=" "))
    print(firstNum + secondNum)


if __name__ == "__main__":
    main()