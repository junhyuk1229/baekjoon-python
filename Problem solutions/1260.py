import sys


def dfsSearch(graphInput, startNode):
    tempStack = [startNode]
    checkedArr = [startNode]
    print(startNode, end=' ')
    while tempStack:
        for conNode in graphInput[tempStack[-1]]:
            if conNode not in checkedArr:
                print(conNode, end=' ')
                tempStack.append(conNode)
                checkedArr.append(conNode)
                break
        if all(nodeNum in checkedArr for nodeNum in graphInput[tempStack[-1]]):
            tempStack.pop(-1)
    print()


def bfsSearch(graphInput, startNode):
    tempQueue = [startNode]
    checkedArr = [startNode]
    while tempQueue:
        for conNode in graphInput[tempQueue[0]]:
            if conNode not in checkedArr:
                checkedArr.append(conNode)
                tempQueue.append(conNode)
        print(tempQueue.pop(0), end=' ')
    print()


def main():
    nodeNum, conNum, startNode = map(int, sys.stdin.readline().split(sep=' '))
    graphNode = {startNode: []}
    for i in range(conNum):
        firstNode, secondNode = map(int, sys.stdin.readline().split(sep=' '))
        if firstNode not in graphNode:
            graphNode[firstNode] = []
        if secondNode not in graphNode:
            graphNode[secondNode] = []
        if firstNode not in graphNode[secondNode]:
            graphNode[secondNode].append(firstNode)
        if secondNode not in graphNode[firstNode]:
            graphNode[firstNode].append(secondNode)
    for i in graphNode:
        graphNode[i].sort()
    dfsSearch(graphNode, startNode)
    bfsSearch(graphNode, startNode)


if __name__ == "__main__":
    main()