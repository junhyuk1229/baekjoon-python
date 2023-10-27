from collections import deque
import sys


DX = [0, 0, 1, -1]
DY = [1, -1, 0, 0]


def mark_air(input_map: list) -> None:
    temp_queue = deque([[0, 0]])
    input_map[0][0] = 3

    while temp_queue:
        temp_x, temp_y = temp_queue.popleft()

        for dx, dy in zip(DX, DY):
            if not 0 <= temp_x + dx < len(input_map):
                continue

            if not 0 <= temp_y + dy < len(input_map[0]):
                continue

            if input_map[temp_x + dx][temp_y + dy] == 0 or input_map[temp_x + dx][temp_y + dy] == 2:
                input_map[temp_x + dx][temp_y + dy] = 3
                temp_queue.append([temp_x + dx, temp_y + dy])

    for temp_x, temp_list in enumerate(input_map):
        for temp_y, temp_num in enumerate(temp_list):
            if temp_num == 3:
                input_map[temp_x][temp_y] = 2

    return


def melt_cheese(input_map: list) -> bool:
    for temp_x, temp_list in enumerate(input_map):
        for temp_y, temp_num in enumerate(temp_list):
            if input_map[temp_x][temp_y] != 1:
                continue

            air_num = 0

            for dx, dy in zip(DX, DY):
                if not 0 <= temp_x + dx < len(input_map):
                    continue

                if not 0 <= temp_y + dy < len(input_map[0]):
                    continue

                if input_map[temp_x + dx][temp_y + dy] == 2:
                    air_num += 1

            if air_num >= 2:
                input_map[temp_x][temp_y] = 3

    is_changed = False

    for temp_x, temp_list in enumerate(input_map):
        for temp_y, temp_num in enumerate(temp_list):
            if temp_num == 3:
                input_map[temp_x][temp_y] = 2
                is_changed = True

    return is_changed


def main() -> None:
    height_num, width_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    input_map = list()

    for _ in range(height_num):
        input_map.append(list(map(int, sys.stdin.readline().rstrip().split(sep=' '))))

    output_num = 0

    while True:
        mark_air(input_map)
        if not melt_cheese(input_map):
            break

        output_num += 1

    print(output_num)

    return


if __name__ == '__main__':
    main()
