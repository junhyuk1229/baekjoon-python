from collections import deque
import sys


def bfsSearch(inputMap, endNum):
    checkMap = [False] * endNum
    checkQueue = deque([0])
    checkMap[0] = True
    while checkQueue:
        tempIndex = checkQueue.popleft()
        for tempNum in inputMap[tempIndex]:
            if tempNum == endNum - 1:
                return 1
            if checkMap[tempNum] is True:
                continue
            checkMap[tempNum] = True
            checkQueue.append(tempNum)
    return 0


def main():
    testNum = int(sys.stdin.readline().rstrip())
    for _ in range(testNum):
        buildNum = int(sys.stdin.readline().rstrip())
        inputPoint = []
        mapInput = {}
        for i in range(buildNum + 2):
            inputPoint.append(list(map(int, sys.stdin.readline().split(sep=' '))))
            mapInput[i] = []
        firstIndex = 0
        while firstIndex < buildNum + 1:
            secondIndex = firstIndex + 1
            while secondIndex < buildNum + 2:
                fx, fy = inputPoint[firstIndex]
                sx, sy = inputPoint[secondIndex]
                if abs(fx - sx) + abs(fy - sy) <= 1000:
                    mapInput[firstIndex].append(secondIndex)
                    mapInput[secondIndex].append(firstIndex)
                secondIndex += 1
            firstIndex += 1
        if bfsSearch(mapInput, buildNum + 2) == 1:
            print('happy')
        else:
            print('sad')


if __name__ == "__main__":
    main()