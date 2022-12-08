import sys
from collections import deque


DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]


def bfsSearch(mapInput, emptyCheck, heightNum, startPoint):
    checkQueue = deque([startPoint])
    emptyCheck[startPoint[0]][startPoint[1]] = 1
    while checkQueue:
        X, Y = map(int, checkQueue.popleft())
        for i in range(4):
            x = X + DX[i]
            y = Y + DY[i]
            if 0 <= x < len(mapInput) and 0 <= y < len(mapInput):
                if mapInput[x][y] < heightNum or emptyCheck[x][y] == 1:
                    continue
                emptyCheck[x][y] = 1
                checkQueue.append([x, y])


def maxIslandCheck(mazeInput, heightArr):
    maxIsland = 0
    for height in heightArr:
        tempIsland = 0
        emptyCheck = []
        for i in range(len(mazeInput)):
            emptyCheck.append([0] * len(mazeInput))
        for x in range(len(mazeInput)):
            for y in range(len(mazeInput)):
                if mazeInput[x][y] < height or emptyCheck[x][y] == 1:
                    continue
                bfsSearch(mazeInput, emptyCheck, height, [x, y])
                tempIsland += 1
        if tempIsland > maxIsland:
            maxIsland = tempIsland
    return maxIsland

def main():
    mapSize = int(sys.stdin.readline().rstrip())
    inputMap = []
    heightArr = deque([])
    for i in range(mapSize):
        tempArr = list(map(int, sys.stdin.readline().split(sep=' ')))
        for j in tempArr:
            if j not in heightArr:
                heightArr.append(j)
        inputMap.append(tempArr)
    print(maxIslandCheck(inputMap, heightArr))

if __name__ == "__main__":
    main()