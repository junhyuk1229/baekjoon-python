import sys


def main():
    while True:
        try:
            inputNum = int(sys.stdin.readline().rstrip())
        except:
            break;
        oneNum = 1
        tempNum = 1
        while tempNum % inputNum != 0:
            tempNum %= inputNum
            tempNum *= 10
            tempNum += 1
            oneNum += 1
        print(oneNum)


if __name__ == "__main__":
    main()