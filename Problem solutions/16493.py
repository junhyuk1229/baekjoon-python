import sys


def main() -> None:
    day_num, input_len = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    output_list = [0] * (day_num + 1)

    for _ in range(input_len):
        temp_day, point_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))

        for temp_index in range(day_num - temp_day + 1):
            to_index = day_num - temp_index
            from_index = day_num - temp_day - temp_index

            output_list[to_index] = max(output_list[to_index], output_list[from_index] + point_num)

    print(output_list[-1])

    return


if __name__ == "__main__":
    main()
