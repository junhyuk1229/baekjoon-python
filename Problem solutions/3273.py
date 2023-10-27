import sys


def main() -> None:
    input_num = int(sys.stdin.readline().rstrip())
    input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    sum_num = int(sys.stdin.readline().rstrip())

    start_index, end_index = 0, input_num - 1
    output_num = 0

    input_list.sort()

    while start_index < end_index:
        if input_list[start_index] + input_list[end_index] == sum_num:
            output_num += 1
            start_index += 1
            end_index -= 1
        elif input_list[start_index] + input_list[end_index] > sum_num:
            end_index -= 1
        else:
            start_index += 1

    print(output_num)

    return


if __name__ == '__main__':
    main()
