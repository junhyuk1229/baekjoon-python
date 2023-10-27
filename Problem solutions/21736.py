from collections import deque
import sys


DX = [0, 0, 1, -1]
DY = [1, -1, 0, 0]


def check_oob(comp_x, comp_y, max_x, max_y):
    if not 0 <= comp_x < max_x:
        return True
    if not 0 <= comp_y < max_y:
        return True

    return False


def get_result(input_map, input_dims, start_loc):
    input_x, input_y = input_dims
    visited_map = [[False] * input_y for _ in range(input_x)]

    visited_map[start_loc[0]][start_loc[1]] = True
    temp_deque = deque([start_loc])

    visited_people = 0

    while temp_deque:
        curr_x, curr_y = temp_deque.pop()
        for dx, dy in zip(DX, DY):
            if check_oob(curr_x + dx, curr_y + dy, input_x, input_y):
                continue

            visit_x = curr_x + dx
            visit_y = curr_y + dy

            if visited_map[visit_x][visit_y]:
                continue

            tile_char = input_map[visit_x][visit_y]

            if tile_char == 'X':
                continue

            if tile_char == 'P':
                visited_people += 1

            visited_map[visit_x][visit_y] = True
            temp_deque.append([visit_x, visit_y])

    return visited_people


def main() -> None:
    input_x, input_y = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    input_map = list()

    for temp_x in range(input_x):
        input_map.append(sys.stdin.readline().rstrip())
        for temp_y in range(input_y):
            if input_map[temp_x][temp_y] == 'I':
                start_loc = [temp_x, temp_y]

    output_num = get_result(input_map, [input_x, input_y], start_loc)

    if output_num == 0:
        print('TT')
    else:
        print(output_num)


if __name__ == '__main__':
    main()
