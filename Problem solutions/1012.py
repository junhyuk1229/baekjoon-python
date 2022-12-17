import sys
from collections import deque


def bfs(input_arr, del_arr, input_x, input_y):
    queue = deque([[input_x, input_y]])
    input_arr[input_x][input_y] = 0
    del_arr.remove([input_x, input_y])
    while queue:
        x, y = queue.popleft()
        if x + 1 != len(input_arr) and input_arr[x + 1][y] == 1:
            queue.append([x + 1, y])
            input_arr[x + 1][y] = 0
            del_arr.remove([x + 1, y])
        if y + 1 != len(input_arr[0]) and input_arr[x][y + 1] == 1:
            queue.append([x, y + 1])
            input_arr[x][y + 1] = 0
            del_arr.remove([x, y + 1])
        if x != 0 and input_arr[x - 1][y] == 1:
            queue.append([x - 1, y])
            input_arr[x - 1][y] = 0
            del_arr.remove([x - 1, y])
        if y != 0 and input_arr[x][y - 1] == 1:
            queue.append([x, y - 1])
            input_arr[x][y - 1] = 0
            del_arr.remove([x, y - 1])


case_num = int(sys.stdin.readline().rstrip())
for _ in range(case_num):
    field_x, field_y, cab_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    cab_arr = [[0 for _ in range(field_y)] for _ in range(field_x)]
    cab_pos = []
    for _ in range(cab_num):
        temp_x, temp_y = map(int, sys.stdin.readline().rstrip().split(sep=' '))
        cab_pos.append([temp_x, temp_y])
        cab_arr[temp_x][temp_y] = 1
    worm_num = 0
    while cab_pos:
        bfs(cab_arr, cab_pos, cab_pos[0][0], cab_pos[0][1])
        worm_num += 1
    print(worm_num)
