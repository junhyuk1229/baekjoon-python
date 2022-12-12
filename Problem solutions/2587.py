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


def main():
    input_arr = [0] * 5
    average_num = 0
    for i in range(5):
        input_arr[i] = int(sys.stdin.readline().rstrip())
        average_num += input_arr[i]
    input_arr = mergeSort(input_arr)
    print("%d\n%d" % (average_num // 5, input_arr[2]))


if __name__ == "__main__":
    main()
