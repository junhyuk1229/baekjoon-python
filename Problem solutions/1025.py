import sys
import math


def check_square(input_num: str, check_set: set) -> None:
    input_num = int(input_num)
    if input_num == round(math.sqrt(input_num)) ** 2:
        check_set.add(input_num)
    return


def check_dir(input_map: list, start_pos: list, d_pos: list, check_set: set, check_str='') -> None:
    if start_pos[0] >= len(input_map) or 0 > start_pos[0] or start_pos[1] >= len(input_map[0]) or 0 > start_pos[1]:
        return
    check_str += input_map[start_pos[0]][start_pos[1]]
    start_pos[0] += d_pos[0]
    start_pos[1] += d_pos[1]
    check_square(check_str, check_set)
    check_dir(input_map, start_pos, d_pos, check_set, check_str)
    return


def main():
    input_height, input_width = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    input_map = [sys.stdin.readline().rstrip() for _ in range(input_height)]
    check_set = set()
    for start_height in range(input_height):
        for start_width in range(input_width):
            for dx in range(-start_height, input_height - start_height):
                for dy in range(-start_width, input_width - start_width):
                    if dx == dy == 0:
                        check_square(input_map[start_height][start_width], check_set)
                        continue
                    check_dir(input_map, [start_height, start_width], [dx, dy], check_set)
    if check_set:
        print(max(check_set))
    else:
        print(-1)
    return


if __name__ == '__main__':
    main()
