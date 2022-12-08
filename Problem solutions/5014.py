import sys
from collections import deque


def bfsSearch(inputArr):
    maxHeight, fromFloor, toFloor, upFloor, downFloor = map(int, inputArr)
    checkQueue = deque([fromFloor])
    distArr = [0] * (maxHeight + 1)
    distArr[fromFloor] = 1
    while distArr[toFloor] == 0 and checkQueue:
        temp = checkQueue.popleft()
        checkNums = [temp - downFloor, temp + upFloor]
        for check in checkNums:
            if check <= 0 or check > maxHeight or distArr[check] != 0:
                continue
            distArr[check] = distArr[temp] + 1
            checkQueue.append(check)
    return distArr[toFloor] - 1


def main():
    inputArr = list(map(int, sys.stdin.readline().split(sep=' ')))
    resultNum = bfsSearch(inputArr)
    if resultNum < 0:
        print('use the stairs')
    else:
        print(resultNum)


if __name__ == "__main__":
    main()