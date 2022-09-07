import sys

def main():
    inputNum = int(sys.stdin.readline().rstrip())
    tempNum = 1
    while (tempNum + 1) * tempNum // 2 < inputNum:
        tempNum += 1
    if tempNum % 2 == 0:
        print(f"{tempNum - (tempNum + 1) * tempNum // 2 + inputNum}/{(tempNum + 1) * tempNum // 2 - inputNum + 1}")
    else:
        print(f"{(tempNum + 1) * tempNum // 2 - inputNum + 1}/{tempNum - (tempNum + 1) * tempNum // 2 + inputNum}")


if __name__ == "__main__":
    main()