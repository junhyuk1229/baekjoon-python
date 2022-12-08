from collections import deque
import sys


DX = [-1, 1, 0, 0]
DY = [0, 0, -1, 1]


def bfsSearch(inputMap, checkQueue, visitMap, startPoint):
    checkQueue.append(startPoint)
    visitMap[startPoint[0]][startPoint[1]] = True
    while checkQueue:
        checkX, checkY = map(int, checkQueue.popleft())
        for i in range(4):
            X = checkX + DX[i]
            Y = checkY + DY[i]
            if inputMap[X][Y] != 0 and visitMap[X][Y] is False:
                checkQueue.append([X, Y])
                visitMap[X][Y] = True
            elif inputMap[X][Y] == 0 and inputMap[checkX][checkY] > 0 and visitMap[X][Y] is False:
                inputMap[checkX][checkY] -= 1


def main():
    mapHeight, mapWidth = map(int, sys.stdin.readline().split(sep=' '))
    inputMap = []
    for _ in range(mapHeight):
        inputMap.append(list(map(int, sys.stdin.readline().split(sep=' '))))
    timePassed = 0
    checkQueue = deque()

    while 1:
        visitMap = []
        for _ in range(mapHeight):
            visitMap.append([False] * mapWidth)
        checkTimes = 0
        for x in range(mapHeight):
            for y in range(mapWidth):
                if inputMap[x][y] == 0 or visitMap[x][y] is True:
                    continue
                bfsSearch(inputMap, checkQueue, visitMap, [x, y])
                checkTimes += 1
        if checkTimes >= 2:
            print(timePassed)
            break
        elif checkTimes == 0:
            print(0)
            break
        timePassed += 1


if __name__ == "__main__":
    main()