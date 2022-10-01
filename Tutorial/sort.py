def mergeSort(inputArr):
    if len(inputArr) == 1:
        return inputArr
    midIndex = len(inputArr) // 2
    firstArr = mergeSort(inputArr[0:midIndex])
    secondArr = mergeSort(inputArr[midIndex:])
    resultArr = []
    firstIndex = secondIndex = 0
    while (firstIndex < len(firstArr)) and (secondIndex < len(secondArr)):
        if firstArr[firstIndex] < secondArr[secondIndex]:
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