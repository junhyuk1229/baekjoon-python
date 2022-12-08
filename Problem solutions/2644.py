import sys


def bfsSearch(inputMap, startNum, endNum):
    genNum = 0
    tempQueue = [startNum]
    nextQueue = []
    checkedArr = [startNum]
    if startNum == endNum:
        return 0
    while tempQueue:
        for conNode in inputMap[tempQueue[0]]:
            if conNode not in checkedArr:
                checkedArr.append(conNode)
                nextQueue.append(conNode)
        tempQueue.pop(0)
        if tempQueue:
            continue
        genNum += 1
        if endNum in nextQueue:
            return genNum
        tempQueue = nextQueue.copy()
        nextQueue = []
    return -1


def main():
    peopleNum = int(sys.stdin.readline().rstrip())
    firstPerson, secondPerson = map(int, sys.stdin.readline().split(sep=' '))
    peopleGraph = {}
    for i in range(peopleNum):
        peopleGraph[i + 1] = []
    conNum = int(sys.stdin.readline().rstrip())
    for _ in range(conNum):
        inputPersons = list(map(int, sys.stdin.readline().split(sep=' ')))
        if inputPersons[1] not in peopleGraph[inputPersons[0]]:
            peopleGraph[inputPersons[0]].append(inputPersons[1])
        if inputPersons[0] not in peopleGraph[inputPersons[1]]:
            peopleGraph[inputPersons[1]].append(inputPersons[0])
    print(bfsSearch(peopleGraph, firstPerson, secondPerson))



if __name__ == "__main__":
    main()