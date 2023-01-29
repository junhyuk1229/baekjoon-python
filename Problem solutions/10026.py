from collections import deque
import sys


DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]


def dfs_normal(map_list, check_map, start_height, start_width):
    temp_queue = deque([[start_height, start_width]])
    check_map[start_height][start_width] = True
    start_color = map_list[start_height][start_width]
    while temp_queue:
        temp_height, temp_width = temp_queue.popleft()
        for dx, dy in zip(DX, DY):
            if temp_height + dx == len(map_list) or temp_width + dy == len(map_list):
                continue
            if temp_height + dx == -1 or temp_width + dy == -1:
                continue
            if check_map[temp_height + dx][temp_width + dy]:
                continue
            if start_color != map_list[temp_height + dx][temp_width + dy]:
                continue
            check_map[temp_height + dx][temp_width + dy] = True
            temp_queue.append([temp_height + dx, temp_width + dy])
    return


def dfs_blind(map_list, check_map, start_height, start_width):
    temp_queue = deque([[start_height, start_width]])
    check_map[start_height][start_width] = True
    if map_list[start_height][start_width] == 'B':
        start_color = 'B'
    else:
        start_color = 'X'
    while temp_queue:
        temp_height, temp_width = temp_queue.popleft()
        for dx, dy in zip(DX, DY):
            if temp_height + dx == len(map_list) or temp_width + dy == len(map_list):
                continue
            if temp_height + dx == -1 or temp_width + dy == -1:
                continue
            if check_map[temp_height + dx][temp_width + dy]:
                continue
            if (map_list[temp_height + dx][temp_width + dy] == 'B') ^ (start_color == 'B'):
                continue
            check_map[temp_height + dx][temp_width + dy] = True
            temp_queue.append([temp_height + dx, temp_width + dy])
    return


def main():
    map_len = int(sys.stdin.readline().rstrip())
    map_list = []
    for _ in range(map_len):
        map_list.append(sys.stdin.readline().rstrip())

    check_map = [[False] * map_len for _ in range(map_len)]
    output_list = []
    temp_output = 0
    for temp_height in range(map_len):
        for temp_width in range(map_len):
            if check_map[temp_height][temp_width]:
                continue
            dfs_normal(map_list, check_map, temp_height, temp_width)
            temp_output += 1
    output_list.append(temp_output)

    check_map = [[False] * map_len for _ in range(map_len)]
    temp_output = 0
    for temp_height in range(map_len):
        for temp_width in range(map_len):
            if check_map[temp_height][temp_width]:
                continue
            dfs_blind(map_list, check_map, temp_height, temp_width)
            temp_output += 1
    output_list.append(temp_output)

    print(' '.join(map(str, output_list)))

    return


if __name__ == "__main__":
    main()
