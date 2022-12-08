from collections import deque
import sys


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


def main():
    caseNum = int(sys.stdin.readline().rstrip())
    checkStack = deque()
    for _ in range(caseNum):
        inputStr = sys.stdin.readline().rstrip()
        if inputStr == 'pop':
            print(pop(checkStack))
        elif inputStr == 'size':
            print(len(checkStack))
        elif inputStr == 'empty':
            print(empty(checkStack))
        elif inputStr == 'top':
            print(peek(checkStack))
        else:
            push(checkStack, inputStr[5:])


if __name__ == "__main__":
    main()