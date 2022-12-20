import sys
from collections import deque


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(world_arr, visit_arr, baby_pos, baby_size, output_arr):
    baby_pos.append([None, None])
    while baby_pos:
        temp_x, temp_y = baby_pos.popleft()
        if temp_x is None:
            return False
        for x, y in zip(dx, dy):
            if temp_x + x >= len(visit_arr) or temp_y + y >= len(visit_arr) or visit_arr[x + temp_x][y + temp_y]:
                continue
            if temp_x + x < 0 or temp_y + y < 0:
                continue
            if world_arr[temp_x + x][temp_y + y] > baby_size:
                visit_arr[temp_x + x][temp_y + y] = True
                continue
            # if food is found
            if 0 < world_arr[temp_x + x][temp_y + y] < baby_size:
                if output_arr[0] == -1 or output_arr[0] * len(world_arr) + output_arr[1] > (temp_x + x) * len(world_arr) + temp_y + y:
                    output_arr[0] = temp_x + x
                    output_arr[1] = temp_y + y
            visit_arr[temp_x + x][temp_y + y] = True
            baby_pos.append([temp_x + x, temp_y + y])
    return output_arr


def find_food(world_arr, baby_pos, baby_size, output_arr):
    visit_arr = [[False] * len(world_arr) for _ in world_arr]
    visit_arr[baby_pos[0][0]][baby_pos[0][1]] = True
    pass_time = 0
    no_food_flag = True
    while baby_pos:
        pass_time += 1
        bfs(world_arr, visit_arr, baby_pos, baby_size, output_arr)
        if output_arr[0] != -1:
            no_food_flag = False
            break
    if no_food_flag:
        return -1
    return pass_time


world_num = int(sys.stdin.readline().rstrip())
world_arr = []
baby_pos = deque()
for x in range(world_num):
    world_arr.append(list(map(int, sys.stdin.readline().rstrip().split(sep=' '))))
    for y in range(world_num):
        if world_arr[x][y] == 9:
            baby_pos.append([x, y])
            world_arr[x][y] = 0

baby_size = 2
food_grow = 2
time_passed = 0
output_arr = [-1, -1]

while True:
    output_time = find_food(world_arr, baby_pos, baby_size, output_arr)
    if output_time == -1:
        break
    time_passed += output_time
    baby_pos = deque([output_arr])
    world_arr[baby_pos[0][0]][baby_pos[0][1]] = 0
    food_grow -= 1
    if food_grow == 0:
        baby_size += 1
        food_grow = baby_size
    output_arr = [-1, -1]

print(time_passed)
