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


def search_half(input_arr, input_num):
    start_index = 0
    middle_index = (len(input_arr) - 1) // 2
    end_index = len(input_arr) - 1
    while start_index <= end_index:
        if input_arr[middle_index] == input_num:
            return True
        if input_arr[middle_index] < input_num:
            start_index = middle_index + 1
        else:
            end_index = middle_index - 1
        middle_index = (start_index + end_index) // 2
    return False

#sets are faster than lists