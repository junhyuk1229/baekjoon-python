import sys
from collections import deque


case_num = int(sys.stdin.readline().rstrip())
for _ in range(case_num):
    instruct_arr = sys.stdin.readline().rstrip()
    arr_len = int(sys.stdin.readline().rstrip())
    input_arr_str = sys.stdin.readline().rstrip()
    input_arr = input_arr_str[1:len(input_arr_str) - 1].split(sep=',')
    temp_queue = deque(input_arr)
    pop_dir = True
    for instruct_char in instruct_arr:
        if instruct_char == 'R':
            # toggle pop_dir
            if pop_dir:
                pop_dir = False
            else:
                pop_dir = True
        else:
            arr_len -= 1
            if arr_len == -1:
                print("error")
                break
            if pop_dir:
                # pop left
                temp_queue.popleft()
            else:
                # pop right
                temp_queue.pop()
    if arr_len == -1:
        continue
    if pop_dir == 1:
        print(f'[{",".join(temp_queue)}]')
    else:
        print(f'[{",".join(list(temp_queue)[::-1])}]')
