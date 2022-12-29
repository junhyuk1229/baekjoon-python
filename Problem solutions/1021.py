import sys
from collections import deque


queue_len, pop_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
queue_arr = deque()
for temp_num in range(queue_len):
    queue_arr.append(temp_num + 1)
pop_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
move_num = 0
for temp_pop in pop_arr:
    temp_index = 0
    while queue_arr[-temp_index] != temp_pop and queue_arr[temp_index] != temp_pop:
        temp_index += 1
    if queue_arr[temp_index] == temp_pop:
        for _ in range(temp_index):
            queue_arr.append(queue_arr.popleft())
    else:
        for _ in range(temp_index):
            queue_arr.appendleft(queue_arr.pop())
    queue_arr.popleft()
    move_num += temp_index
print(move_num)
