import sys

def main():
    inputNum = int(sys.stdin.readline().rstrip())
    tempNum = 1
    while 3 * tempNum * (tempNum - 1) + 2 <= inputNum:
        tempNum += 1
    print(tempNum)


if __name__ == "__main__":
    main()