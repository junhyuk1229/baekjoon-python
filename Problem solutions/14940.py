from collections import deque
import sys


DX = [0, 0, 1, -1]
DY = [1, -1, 0, 0]


def check_oob(input_map, check_x, check_y):
    if 0 > check_x or check_x >= len(input_map):
        return -1
    if 0 > check_y or check_y >= len(input_map[0]):
        return -1
    return input_map[check_x][check_y]


def bfs(input_map: list, visit_map: list, start_list: deque) -> None:
    loop_num = 1

    while start_list:
        output_list = deque()

        while start_list:
            temp_x, temp_y = start_list.pop()

            for dx, dy in zip(DX, DY):
                if check_oob(input_map, temp_x + dx, temp_y + dy) == 1:
                    visit_map[temp_x + dx][temp_y + dy] = loop_num
                    input_map[temp_x + dx][temp_y + dy] = 2
                    output_list.append([temp_x + dx, temp_y + dy])

        start_list = output_list
        loop_num += 1

    return


def main() -> None:
    input_x, input_y = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    input_map = []

    visit_map = [[-1] * input_y for _ in range(input_x)]

    for x in range(input_x):
        input_map.append(list(map(int, sys.stdin.readline().rstrip().split(sep=' '))))
        for y in range(input_y):
            if input_map[x][y] == 2:
                start_x = x
                start_y = y
            if input_map[x][y] == 0:
                visit_map[x][y] = 0

    visit_map[start_x][start_y] = 0

    bfs(input_map, visit_map, deque([[start_x, start_y]]))

    for temp_line in visit_map:
        print(' '.join(map(str, temp_line)))


if __name__ == '__main__':
    main()
