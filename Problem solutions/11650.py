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
        if firstArr[firstIndex][0] < secondArr[secondIndex][0] or\
        (firstArr[firstIndex][0] == secondArr[secondIndex][0] and firstArr[firstIndex][1] < secondArr[secondIndex][1]):
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
        inputArr.append(list(map(int, sys.stdin.readline().split(sep=' '))))
    resultArr = mergeSort(inputArr)
    for i in resultArr:
        for j in i:
            print(j, end=' ')
        print()



if __name__ == "__main__":
    main()