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
        if firstArr[firstIndex][0] <= secondArr[secondIndex][0]:
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
    inputArr = []
    for i in range(arrLen):
        inputNum, inputStr = map(str, sys.stdin.readline().split(sep=" "))
        inputArr.append([int(inputNum), inputStr.rstrip()])

    outputArr = mergeSort(inputArr)

    for i in outputArr:
        for j in i:
            print(j, end=' ')
        print()

if __name__ == "__main__":
    main()