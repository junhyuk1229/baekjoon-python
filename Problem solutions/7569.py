from collections import deque
import sys

def bfsSearch(boxInput, tempQueue):
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    while tempQueue:
        H, D, W = tempQueue.popleft()
        for i in range(6):
            h = H + dx[i]
            d = D + dy[i]
            w = W + dz[i]
            if 0 <= h < len(boxInput) and 0 <= d < len(boxInput[0]) and 0 <= w < len(boxInput[0][0]) and boxInput[h][d][w] == 0:
                tempQueue.append([h, d, w])
                boxInput[h][d][w] = boxInput[H][D][W] + 1

def main():
    boxWidth, boxDepth, boxHeight = map(int, sys.stdin.readline().split(sep=' '))
    inputMap = []
    inputStart = deque([])
    for i in range(boxHeight):
        inputMap.append([])
        for j in range(boxDepth):
            inputArr = list(map(int, sys.stdin.readline().split(sep=' ')))
            inputMap[i].append(inputArr)
            for k in range(boxWidth):
                if inputMap[i][j][k] == 1:
                    inputStart.append([i, j, k])
    bfsSearch(inputMap, inputStart)
    maxNum = 0
    for i in inputMap:
        for j in i:
            for k in j:
                if k == 0:
                    print(-1)
                    return
                if k - 1 > maxNum:
                    maxNum = k - 1
    print(maxNum)



if __name__ == "__main__":
    main()