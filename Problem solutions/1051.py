from collections import deque
import sys


def main() -> None:
    list_height, list_width = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    input_map = [[int(temp_char) for temp_char in sys.stdin.readline().rstrip()] for _ in range(list_height)]

    output_size = min(list_height, list_width)

    while output_size > 1:
        for temp_height in range(list_height - output_size + 1):
            for temp_width in range(list_width - output_size + 1):
                start_num = input_map[temp_height][temp_width]

                if start_num != input_map[temp_height + output_size - 1][temp_width]:
                    continue
                if start_num != input_map[temp_height][temp_width + output_size - 1]:
                    continue
                if start_num != input_map[temp_height + output_size - 1][temp_width + output_size - 1]:
                    continue

                print(output_size ** 2)

                return

        output_size -= 1

    print(1)

    return


if __name__ == '__main__':
    main()
