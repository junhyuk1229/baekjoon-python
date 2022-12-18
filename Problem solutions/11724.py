import sys
from collections import deque


def dfs(con_dict, visit_arr, start_node):
    temp_queue = deque([start_node])
    while temp_queue:
        temp_index = temp_queue.popleft()
        for con_index in con_dict[temp_index]:
            if visit_arr[con_index] == 1:
                continue
            visit_arr[con_index] = 1
            temp_queue.append(con_index)


def search_seg(con_dict, visit_arr):
    temp_output = 0
    temp_index = 1
    while temp_index < len(visit_arr):
        if visit_arr[temp_index] == 0:
            dfs(con_dict, visit_arr, temp_index)
            temp_output += 1
        temp_index += 1
    return temp_output


point_num, line_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
input_dict = dict()
for temp_index in range(point_num):
    input_dict[temp_index + 1] = []
for _ in range(line_num):
    first_node, second_node = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    input_dict[first_node].append(second_node)
    input_dict[second_node].append(first_node)
visit_arr = [0 for _ in range(point_num + 1)]
print(search_seg(input_dict, visit_arr))
