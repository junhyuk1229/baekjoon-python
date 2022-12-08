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