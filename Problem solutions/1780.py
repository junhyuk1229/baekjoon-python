import sys
from collections import deque


def dfs(input_arr, input_size):
    # output used neg, zero, one in order
    output_arr = [0, 0, 0]
    temp_stack = deque([input_arr])
    while temp_stack:
        temp_arr = temp_stack.pop()
        one_flag = False
        zero_flag = False
        neg_flag = False

        # check for ones and zeros and negative ones
        for temp_list in temp_arr:
            if 1 in temp_list:
                one_flag = True
            if 0 in temp_list:
                zero_flag = True
            if -1 in temp_list:
                neg_flag = True
            if (one_flag and zero_flag) or (one_flag and neg_flag) or (neg_flag and zero_flag):
                break
        if not ((one_flag and zero_flag) or (one_flag and neg_flag) or (neg_flag and zero_flag)):
            if zero_flag:
                output_arr[1] += 1
            elif one_flag:
                output_arr[2] += 1
            else:
                output_arr[0] += 1
            continue

        stack_input_arr = []
        for _ in range(9):
            stack_input_arr.append([])
        for temp_height, temp_list in enumerate(temp_arr):
            for temp_num in range(3):
                start_index = temp_num * len(temp_list) // 3
                end_index = (temp_num + 1) * len(temp_list) // 3
                input_index = temp_height // (len(temp_list) // 3) * 3
                stack_input_arr[input_index + temp_num].append(temp_list[start_index:end_index])
        for temp_list in stack_input_arr[::-1]:
            temp_stack.append(temp_list)

    for temp_num in output_arr:
        print(temp_num)


input_len = int(sys.stdin.readline().rstrip())
input_arr = []
for _ in range(input_len):
    input_arr.append(list(map(int, list(sys.stdin.readline().rstrip().split(sep=' ')))))
dfs(input_arr, input_len)
