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
        if len(firstArr[firstIndex]) < len(secondArr[secondIndex]) or (len(firstArr[firstIndex]) == len(secondArr[secondIndex]) and firstArr[firstIndex] < secondArr[secondIndex]):
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
        inputArr.append(sys.stdin.readline().rstrip())
    resultArr = mergeSort(inputArr)

    dupCheck = None
    for i in resultArr:
        if dupCheck != i:
            print(i)
            dupCheck = i



if __name__ == "__main__":
    main()