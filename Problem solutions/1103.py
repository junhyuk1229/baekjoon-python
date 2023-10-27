from collections import deque
import sys


DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]


sys.setrecursionlimit(1000000000)


def dfs(input_stack: deque, input_map: list, visited_map: list, dp_map: list):
    temp_x, temp_y = input_stack[-1]
    map_x, map_y = len(input_map), len(input_map[0])
    cur_value = int(input_map[temp_x][temp_y])
    output_num = len(input_stack)

    for dx, dy in zip(DX, DY):
        dx *= cur_value
        dy *= cur_value

        if not 0 <= temp_x + dx < map_x:
            continue

        if not 0 <= temp_y + dy < map_y:
            continue

        if input_map[temp_x + dx][temp_y + dy] == 'H':
            continue

        if visited_map[temp_x + dx][temp_y + dy]:
            return -1

        if dp_map[temp_x + dx][temp_y + dy] != 0:
            output_num = max(output_num, len(input_stack) + dp_map[temp_x + dx][temp_y + dy] + 1)
            continue

        visited_map[temp_x + dx][temp_y + dy] = True
        input_stack.append([temp_x + dx, temp_y + dy])

        temp_num = dfs(input_stack, input_map, visited_map, dp_map)

        if temp_num == -1:
            return -1

        output_num = max(output_num, temp_num)

        visited_map[temp_x + dx][temp_y + dy] = False
        input_stack.pop()

    dp_map[temp_x][temp_y] = output_num - len(input_stack)

    return output_num


def main() -> None:
    input_height, input_width = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    input_map = [sys.stdin.readline().rstrip() for _ in range(input_height)]
    visited_map = [[False] * input_width for _ in range(input_height)]
    dp_map = [[0] * input_width for _ in range(input_height)]
    visited_map[0][0] = True

    print(dfs(deque([[0, 0]]), input_map, visited_map, dp_map))

    return


if __name__ == '__main__':
    main()
