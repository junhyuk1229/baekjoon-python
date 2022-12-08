import sys
from collections import deque


def push(input_queue, input_num):
    input_queue.append(input_num)


def pop(input_queue):
    if empty(input_queue):
        return -1
    return input_queue.popleft()


def size(input_queue):
    return len(input_queue)


def empty(input_queue):
    if size(input_queue):
        return 0
    return 1


def front(input_queue):
    if empty(input_queue):
        return -1
    temp_num = pop(input_queue)
    input_queue.appendleft(temp_num)
    return temp_num


def back(input_queue):
    if empty(input_queue):
        return -1
    temp_num = input_queue.pop()
    input_queue.append(temp_num)
    return temp_num


def main():
    input_num = int(sys.stdin.readline().rstrip())
    input_queue = deque()
    for _ in range(input_num):
        input_arr = list(sys.stdin.readline().rstrip().split(sep=' '))
        if input_arr[0] == "push":
            push(input_queue, int(input_arr[1]))
        elif input_arr[0] == "pop":
            print(pop(input_queue))
        elif input_arr[0] == "size":
            print(size(input_queue))
        elif input_arr[0] == "empty":
            print(empty(input_queue))
        elif input_arr[0] == "front":
            print(front(input_queue))
        elif input_arr[0] == "back":
            print(back(input_queue))


if __name__ == "__main__":
    main()
