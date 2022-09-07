import sys

def main():
    inputNum = int(sys.stdin.readline().rstrip())
    resultNum = 0
    for i in range(inputNum):
        checkFlag = 1
        inputStr = sys.stdin.readline().rstrip()
        prevChar = None
        checkArr = []
        for j in range(len(inputStr)):
            if inputStr[j] in checkArr and inputStr[j] != prevChar:
                checkFlag = 0
                break
            if inputStr[j] != prevChar:
                checkArr.append(inputStr[j])
                prevChar = inputStr[j]
        if checkFlag == 1:
            resultNum += 1
    print(resultNum)


if __name__ == "__main__":
    main()