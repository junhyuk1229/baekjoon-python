import sys
from collections import deque


input_arr = list(sys.stdin.readline().rstrip())
front_arr = deque(input_arr)
back_arr = deque()
instruct_num = int(sys.stdin.readline().rstrip())


for _ in range(instruct_num):
    instruct_arr = list(sys.stdin.readline().rstrip().split(sep=' '))
    if instruct_arr[0] == 'L':
        if len(front_arr) == 0:
            continue
        back_arr.appendleft(front_arr.pop())
    elif instruct_arr[0] == 'D':
        if len(back_arr) == 0:
            continue
        front_arr.append(back_arr.popleft())
    elif instruct_arr[0] == 'B':
        if len(front_arr) == 0:
            continue
        front_arr.pop()
    else:
        front_arr.append(instruct_arr[1])


while front_arr:
    print(front_arr.popleft(), end='')
while back_arr:
    print(back_arr.popleft(), end='')
