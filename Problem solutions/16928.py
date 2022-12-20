import sys
from collections import deque


def bfs(start_arr, visit_arr, map_arr):
    output_arr = deque()
    while start_arr:
        temp_pos = start_arr.pop()
        for next_pos in range(temp_pos + 1, temp_pos + 7):
            if next_pos > 100:
                break
            if visit_arr[next_pos]:
                continue
            visit_arr[next_pos] = True
            if next_pos in map_arr:
                visit_arr[map_arr[next_pos]] = True
                output_arr.append(map_arr[next_pos])
                continue
            output_arr.append(next_pos)
    return output_arr.copy()


ladder_num, snake_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
map_arr = dict()
for _ in range(ladder_num + snake_num):
    key, value = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    map_arr[key] = value
visit_arr = [False] * 101
move_count = 0
start_arr = deque([1])
while not visit_arr[100]:
    start_arr = bfs(start_arr, visit_arr, map_arr)
    move_count += 1
print(move_count)
