import sys


def bfsSearch(mazeInput):
    distNum = 1
    tempQueue = [[0, 0]]
    sideQueue = []
    checkedArr = [[0, 0]]
    while tempQueue:
        #Up
        if [tempQueue[0][0] - 1, tempQueue[0][1]] not in checkedArr and tempQueue[0][0] != 0 and mazeInput[tempQueue[0][0] - 1][tempQueue[0][1]] == 1:
            sideQueue.append([tempQueue[0][0] - 1, tempQueue[0][1]])
            checkedArr.append([tempQueue[0][0] - 1, tempQueue[0][1]])
        #Down
        if [tempQueue[0][0] + 1, tempQueue[0][1]] not in checkedArr and tempQueue[0][0] != len(mazeInput) - 1 and mazeInput[tempQueue[0][0] + 1][tempQueue[0][1]] == 1:
            sideQueue.append([tempQueue[0][0] + 1, tempQueue[0][1]])
            checkedArr.append([tempQueue[0][0] + 1, tempQueue[0][1]])
        #Left
        if [tempQueue[0][0], tempQueue[0][1] - 1] not in checkedArr and tempQueue[0][1] != 0 and mazeInput[tempQueue[0][0]][tempQueue[0][1] - 1] == 1:
            sideQueue.append([tempQueue[0][0], tempQueue[0][1] - 1])
            checkedArr.append([tempQueue[0][0], tempQueue[0][1] - 1])
        #Right
        if [tempQueue[0][0], tempQueue[0][1] + 1] not in checkedArr and tempQueue[0][1] != len(mazeInput[0]) - 1 and mazeInput[tempQueue[0][0]][tempQueue[0][1] + 1] == 1:
            sideQueue.append([tempQueue[0][0], tempQueue[0][1] + 1])
            checkedArr.append([tempQueue[0][0], tempQueue[0][1] + 1])
        tempQueue.pop(0)
        if tempQueue:
            continue
        distNum += 1
        if [len(mazeInput) - 1, len(mazeInput[0]) - 1] in sideQueue:
            return distNum
        tempQueue = sideQueue.copy()
        sideQueue = []


def main():
    mazeHeight, mazeWidth = map(int, sys.stdin.readline().split(sep=' '))
    mazeMap = []
    for i in range(mazeHeight):
        mazeMap.append([])
        inputMaze = sys.stdin.readline().rstrip()
        for j in range(mazeWidth):
            mazeMap[i].append(ord(inputMaze[j]) - 48)

    print(bfsSearch(mazeMap))


if __name__ == "__main__":
    main()