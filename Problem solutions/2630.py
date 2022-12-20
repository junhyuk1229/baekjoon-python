import sys
from collections import deque


def dfs(input_arr):
    temp_queue = deque([input_arr])
    zero_num = 0
    one_num = 0
    while temp_queue:
        temp_arr = temp_queue.popleft()
        zero_flag = False
        one_flag = False
        for i in temp_arr:
            if 0 in i:
                zero_flag = True
            if 1 in i:
                one_flag = True
            if zero_flag and one_flag:
                break
        if not (zero_flag and one_flag):
            if zero_flag:
                zero_num += 1
            else:
                one_num += 1
            continue
        first_arr = []
        second_arr = []
        third_arr = []
        forth_arr = []
        for index, x in enumerate(temp_arr):
            if index < len(temp_arr) // 2:
                first_arr.append(x[:len(temp_arr) // 2])
                second_arr.append(x[len(temp_arr) // 2:])
            else:
                third_arr.append(x[:len(temp_arr) // 2])
                forth_arr.append(x[len(temp_arr) // 2:])
        temp_queue.append(first_arr)
        temp_queue.append(second_arr)
        temp_queue.append(third_arr)
        temp_queue.append(forth_arr)
    print(f"{zero_num}\n{one_num}")


input_size = int(sys.stdin.readline().rstrip())
input_arr = []
for _ in range(input_size):
    input_arr.append(list(map(int, sys.stdin.readline().rstrip().split(sep=' '))))
dfs(input_arr)
