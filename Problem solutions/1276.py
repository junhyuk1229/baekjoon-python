from collections import defaultdict
import sys


def main() -> None:
    platform_num = int(sys.stdin.readline().rstrip())

    platform_list = list()

    for _ in range(platform_num):
        platform_list.append(list(map(int, sys.stdin.readline().rstrip().split(sep=' '))))

    platform_list.sort(key=lambda x: x[0])

    platform_dict = defaultdict(int)
    output_num = 0

    for temp_height, start_x, end_x in platform_list:
        output_num += 2 * temp_height - platform_dict[start_x] - platform_dict[end_x - 1]

        for temp_x in range(start_x, end_x):
            platform_dict[temp_x] = temp_height

    print(output_num)

    return


if __name__ == '__main__':
    main()
