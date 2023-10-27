from itertools import combinations
import math
import sys


def main() -> None:
    case_num = int(sys.stdin.readline().rstrip())

    for _ in range(case_num):
        point_num = int(sys.stdin.readline().rstrip())
        point_list = [list(map(int, sys.stdin.readline().rstrip().split(sep=' '))) for _ in range(point_num)]

        input_list = [i for i in range(point_num)]
        min_output = math.inf

        x_sum = sum([temp_point[0] for temp_point in point_list])
        y_sum = sum([temp_point[1] for temp_point in point_list])

        for first_point_index in combinations(input_list, point_num // 2):
            first_point_list = [point_list[point_index] for point_index in first_point_index]

            dx_num = x_sum - 2 * sum([temp_point[0] for temp_point in first_point_list])
            dy_num = y_sum - 2 * sum([temp_point[1] for temp_point in first_point_list])

            min_output = min(min_output, math.sqrt(dx_num ** 2 + dy_num ** 2))

        print(min_output)

    return


if __name__ == '__main__':
    main()
