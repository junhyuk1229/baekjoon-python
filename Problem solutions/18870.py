import sys


def mergeSort(inputArr):
    if len(inputArr) == 1:
        return inputArr
    midIndex = len(inputArr) // 2
    firstArr = mergeSort(inputArr[0:midIndex])
    secondArr = mergeSort(inputArr[midIndex:])
    resultArr = []
    firstIndex = secondIndex = 0
    while (firstIndex < len(firstArr)) and (secondIndex < len(secondArr)):
        if firstArr[firstIndex] <= secondArr[secondIndex]:
            resultArr.append(firstArr[firstIndex])
            firstIndex += 1
        else:
            resultArr.append(secondArr[secondIndex])
            secondIndex += 1
    if secondIndex == len(secondArr):
        while firstIndex < len(firstArr):
            resultArr.append(firstArr[firstIndex])
            firstIndex += 1
    else:
        while secondIndex < len(secondArr):
            resultArr.append(secondArr[secondIndex])
            secondIndex += 1
    return resultArr


def main():
    arrLen = int(sys.stdin.readline().rstrip())
    inputArr = list(map(int, sys.stdin.readline().split(sep=' ')))

    resultArr = mergeSort(inputArr)

    checkDict = {}
    tempIndex = 0
    pastNum = None
    for i in resultArr:
        if pastNum != i:
            checkDict[i] = tempIndex
            tempIndex += 1
            pastNum = i

    for i in inputArr:
        print(checkDict[i], end=' ')

if __name__ == "__main__":
    main()