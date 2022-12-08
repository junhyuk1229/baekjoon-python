import sys


def dfsSearch(graphInput):
    tempStack = [0]
    checkedArr = [0]
    infectNum = 0
    while tempStack:
        for conNode in graphInput[tempStack[-1]]:
            if conNode not in checkedArr:
                infectNum += 1
                tempStack.append(conNode)
                checkedArr.append(conNode)
                break
        if all(nodeNum in checkedArr for nodeNum in graphInput[tempStack[-1]]):
            tempStack.pop(-1)
    return infectNum


def main():
    nodeNum = int(sys.stdin.readline().rstrip())
    nodeMap = {}
    for i in range(nodeNum):
        nodeMap[i] = []
    connectNum = int(sys.stdin.readline().rstrip())
    for i in range(connectNum):
        inputCon = list(map(int, sys.stdin.readline().split(sep=' ')))
        if inputCon[0] - 1 not in nodeMap[inputCon[1] - 1]:
            nodeMap[inputCon[1] - 1].append(inputCon[0] - 1)
        if inputCon[1] - 1 not in nodeMap[inputCon[0] - 1]:
            nodeMap[inputCon[0] - 1].append(inputCon[1] - 1)

    print(dfsSearch(nodeMap))

if __name__ == "__main__":
    main()