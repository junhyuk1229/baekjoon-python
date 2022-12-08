import sys


def mergeSort(inputArr):
    if len(inputArr[0]) == 1:
        return inputArr
    midIndex = (len(inputArr[0]) + 1) // 2
    firstArr = mergeSort(list([inputArr[0][0:midIndex], inputArr[1], inputArr[2]]))
    secondArr = mergeSort(list([inputArr[0][midIndex:], firstArr[1], firstArr[2]]))
    resultArr = []
    firstIndex = secondIndex = 0
    while (firstIndex < len(firstArr[0])) and (secondIndex < len(secondArr[0])):
        if firstArr[0][firstIndex] < secondArr[0][secondIndex]:
            resultArr.append(firstArr[0][firstIndex])
            firstIndex += 1
        else:
            resultArr.append(secondArr[0][secondIndex])
            secondIndex += 1
        secondArr[1] -= 1
    if secondIndex == len(secondArr[0]):
        while firstIndex < len(firstArr[0]):
            resultArr.append(firstArr[0][firstIndex])
            firstIndex += 1
            secondArr[1] -= 1
    else:
        while secondIndex < len(secondArr[0]):
            resultArr.append(secondArr[0][secondIndex])
            secondIndex += 1
            secondArr[1] -= 1
    if secondArr[1] <= 0 and secondArr[2] is None:
        secondArr[2] = resultArr[secondArr[1] - 1]
    return list([resultArr, secondArr[1], secondArr[2]])


def main():
    arrLen, checkNum = map(int, sys.stdin.readline().split(sep=' '))
    sortArr = list(map(int, sys.stdin.readline().split(sep=' ')))
    inputArr = [sortArr, checkNum, None]

    resultArr = mergeSort(inputArr)
    if resultArr[2] is not None:
        print(resultArr[2])
    else:
        print(-1)


if __name__ == "__main__":
    main()