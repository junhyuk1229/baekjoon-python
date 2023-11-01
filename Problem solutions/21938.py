from collections import deque
import sys


DX = [0, 0, 1, -1]
DY = [1, -1, 0, 0]


def main() -> None:
    input_height, input_width = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    input_list = list()

    for temp_height in range(input_height):
        input_list.append(list())
        temp_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))

        for temp_index in range(0, len(temp_list), 3):
            input_list[temp_height].append(sum(temp_list[temp_index:temp_index + 3]) / 3)

    comp_num = int(sys.stdin.readline().rstrip())

    visited_map = [[False] * input_width for _ in range(input_height)]
    output_num = 0

    for temp_height, temp_line in enumerate(visited_map):
        for temp_width, _ in enumerate(temp_line):
            if visited_map[temp_height][temp_width]:
                continue

            if input_list[temp_height][temp_width] < comp_num:
                visited_map[temp_height][temp_width] = True
                continue

            output_num += 1
            check_queue = deque([[temp_height, temp_width]])

            while check_queue:
                temp_x, temp_y = check_queue.pop()

                for dx, dy in zip(DX, DY):
                    comp_x = temp_x + dx
                    comp_y = temp_y + dy

                    if not 0 <= comp_x < input_height or not 0 <= comp_y < input_width:
                        continue

                    if visited_map[comp_x][comp_y]:
                        continue

                    visited_map[comp_x][comp_y] = True

                    if input_list[comp_x][comp_y] < comp_num:
                        continue

                    check_queue.append([comp_x, comp_y])

    print(output_num)

    return


if __name__ == "__main__":
    main()
