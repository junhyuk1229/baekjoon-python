import sys


def findJack(checkArr, checkNum):
    tempNum = 0
    i = 0
    while i < len(checkArr) - 2:
        j = i + 1
        while j < len(checkArr) - 1:
            k = j + 1
            while k < len(checkArr):
                tempCheckNum = checkArr[i] + checkArr[j] + checkArr[k]
                if tempCheckNum > tempNum and tempCheckNum <= checkNum:
                    tempNum = tempCheckNum
                k += 1
            j += 1
        i += 1
    return tempNum


def main():
    arrLen, checkNum = map(int, sys.stdin.readline().split(sep=' '))
    inputArr = list(map(int, sys.stdin.readline().split(sep=' ')))

    outputNum = findJack(inputArr, checkNum)
    print(outputNum)


if __name__ == "__main__":
    main()