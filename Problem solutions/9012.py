import sys


def main():
    caseNum = int(sys.stdin.readline().rstrip())
    for _ in range(caseNum):
        inputArr = sys.stdin.readline().rstrip()
        tempNum = 0
        for checkChar in inputArr:
            if checkChar == '(':
                tempNum += 1
            else:
                tempNum -= 1
            if tempNum < 0:
                break
        if tempNum != 0:
            print("NO")
        else:
            print("YES")


if __name__ == "__main__":
    main()