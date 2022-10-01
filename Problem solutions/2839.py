import sys


def main():
    inputNum = int(sys.stdin.readline().rstrip())
    fiveNum = inputNum // 5
    inputNum %= 5
    while fiveNum >= 0 and inputNum % 3 != 0:
        fiveNum -= 1
        inputNum += 5
    if fiveNum < 0:
        print(-1)
    else:
        print(fiveNum + inputNum // 3)


if __name__ == "__main__":
    main()