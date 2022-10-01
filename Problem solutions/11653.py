import sys


def main():
    inputNum = int(sys.stdin.readline().rstrip())
    tempNum = 2
    while inputNum > 1:
        while inputNum % tempNum == 0:
            inputNum //= tempNum
            print(tempNum)
        tempNum += 1


if __name__ == "__main__":
    main()