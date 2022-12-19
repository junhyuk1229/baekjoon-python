import sys
from collections import deque


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(input_map, temp_queue, input_size):
    output_queue = deque()
    while temp_queue:
        temp_node = temp_queue.popleft()
        for x, y in zip(dx, dy):
            if 0 > x + temp_node[0] or x + temp_node[0] >= input_size[0]:
                continue
            if 0 > y + temp_node[1] or y + temp_node[1] >= input_size[1]:
                continue
            if input_map[x + temp_node[0]][y + temp_node[1]] != 0:
                continue
            input_map[x + temp_node[0]][y + temp_node[1]] = 1
            output_queue.append([x + temp_node[0], y + temp_node[1]])
    return output_queue


width_num, height_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
input_arr = []
zero_num = 0
start_node = deque()
for temp_height in range(height_num):
    input_arr.append(list(map(int, sys.stdin.readline().rstrip().split(sep=' '))))
    for temp_width, temp_num in enumerate(input_arr[temp_height]):
        if temp_num == 0:
            zero_num += 1
        if temp_num == 1:
            start_node.append([temp_height, temp_width])
loop_num = 0
while len(start_node) != 0 and zero_num != 0:
    start_node = dfs(input_arr, start_node, [height_num, width_num])
    zero_num -= len(start_node)
    loop_num += 1
if zero_num != 0:
    print(-1)
else:
    print(loop_num)
