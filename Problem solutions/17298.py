import sys
from collections import deque


arr_len = int(sys.stdin.readline().rstrip())
input_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
temp_stack = deque()
stack_len = 0
output_arr = [-1] * arr_len


for temp_arr in enumerate(input_arr):
    while stack_len != 0 and temp_stack[-1][1] < temp_arr[1]:
        output_arr[(temp_stack.pop())[0]] = temp_arr[1]
        stack_len -= 1
    temp_stack.append(temp_arr)
    stack_len += 1


print(' '.join(map(str, output_arr)))
