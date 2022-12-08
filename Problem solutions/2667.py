import sys


def bfsSearch(mazeInput, startCord):
    tempQueue = [startCord]
    sideQueue = []
    checkedArr = [startCord]
    mazeInput[startCord[0]][startCord[1]] = 0
    totalNum = 1
    while tempQueue:
        #Up
        if [tempQueue[0][0] - 1, tempQueue[0][1]] not in checkedArr and tempQueue[0][0] != 0 and mazeInput[tempQueue[0][0] - 1][tempQueue[0][1]] == 1:
            sideQueue.append([tempQueue[0][0] - 1, tempQueue[0][1]])
            checkedArr.append([tempQueue[0][0] - 1, tempQueue[0][1]])
            mazeInput[tempQueue[0][0] - 1][tempQueue[0][1]] = 0
            totalNum += 1
        #Down
        if [tempQueue[0][0] + 1, tempQueue[0][1]] not in checkedArr and tempQueue[0][0] != len(mazeInput) - 1 and mazeInput[tempQueue[0][0] + 1][tempQueue[0][1]] == 1:
            sideQueue.append([tempQueue[0][0] + 1, tempQueue[0][1]])
            checkedArr.append([tempQueue[0][0] + 1, tempQueue[0][1]])
            mazeInput[tempQueue[0][0] + 1][tempQueue[0][1]] = 0
            totalNum += 1
        #Left
        if [tempQueue[0][0], tempQueue[0][1] - 1] not in checkedArr and tempQueue[0][1] != 0 and mazeInput[tempQueue[0][0]][tempQueue[0][1] - 1] == 1:
            sideQueue.append([tempQueue[0][0], tempQueue[0][1] - 1])
            checkedArr.append([tempQueue[0][0], tempQueue[0][1] - 1])
            mazeInput[tempQueue[0][0]][tempQueue[0][1] - 1] = 0
            totalNum += 1
        #Right
        if [tempQueue[0][0], tempQueue[0][1] + 1] not in checkedArr and tempQueue[0][1] != len(mazeInput[0]) - 1 and mazeInput[tempQueue[0][0]][tempQueue[0][1] + 1] == 1:
            sideQueue.append([tempQueue[0][0], tempQueue[0][1] + 1])
            checkedArr.append([tempQueue[0][0], tempQueue[0][1] + 1])
            mazeInput[tempQueue[0][0]][tempQueue[0][1] + 1] = 0
            totalNum += 1
        tempQueue.pop(0)
        if tempQueue:
            continue
        tempQueue = sideQueue.copy()
        sideQueue = []
    return totalNum


def main():
    mapSize = int(sys.stdin.readline().rstrip())
    nodeMap = []
    for i in range(mapSize):
        nodeMap.append([])
        inputNum = sys.stdin.readline().rstrip()
        for j in range(mapSize):
            nodeMap[i].append(ord(inputNum[j]) - 48)
    outputList = []
    for i in range(mapSize):
        for j in range(mapSize):
            if nodeMap[i][j] == 1:
                outputList.append(bfsSearch(nodeMap, [i, j]))
    print(len(outputList))
    outputList.sort()
    for i in outputList:
        print(i)


if __name__ == "__main__":
    main()