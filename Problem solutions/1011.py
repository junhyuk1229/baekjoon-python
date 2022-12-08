import sys
import math


def main():
    case_num = int(sys.stdin.readline())
    for _ in range(case_num):
        start_pos, end_pos = map(int, sys.stdin.readline().split(sep=' '))
        diff_pos = end_pos - start_pos
        max_index = math.floor(math.sqrt(diff_pos))
        if diff_pos == max_index ** 2:
            print(2 * max_index - 1)
        elif diff_pos <= max_index ** 2 + max_index:
            print(2 * max_index)
        else:
            print(2 * max_index + 1)


if __name__ == "__main__":
    main()
