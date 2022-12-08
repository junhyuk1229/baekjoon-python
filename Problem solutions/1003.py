import sys


globalArr = []


def fiboNum(inputNum):
    if inputNum < len(globalArr):
        return globalArr[inputNum]
    else:
        while inputNum >= len(globalArr):
            globalArr.append([globalArr[-1][0] + globalArr[-2][0], globalArr[-1][1] + globalArr[-2][1]])
        return globalArr[inputNum]

def main():
    globalArr.append([1, 0])
    globalArr.append([0, 1])
    caseNum = int(sys.stdin.readline().rstrip())
    for i in range(caseNum):
        inputNum = int(sys.stdin.readline().rstrip())
        outputNum = fiboNum(inputNum)
        print(outputNum[0], outputNum[1])




if __name__ == "__main__":
    main()