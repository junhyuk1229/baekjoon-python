def push(inputQueue, inputNum):
    inputQueue.append(inputNum)


def pop(inputQueue):
    if empty(inputQueue):
        return -1
    return inputQueue.pop()


def peek(inputQueue):
    if empty(inputQueue):
        return -1
    return inputQueue[-1]


def empty(inputQueue):
    if len(inputQueue) == 0:
        return 1
    else:
        return 0