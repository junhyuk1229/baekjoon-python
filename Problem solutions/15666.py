import sys


def recur_print(input_list, start_index, output_len, print_arr='') -> None:
    if output_len == 0:
        print(print_arr)
        return
    for temp_index, temp_val in enumerate(input_list[start_index:]):
        recur_print(input_list, start_index + temp_index, output_len - 1, print_arr + "{0} ".format(temp_val))
    return


def main() -> None:
    input_len, output_len = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    input_list = list(set(map(int, sys.stdin.readline().rstrip().split(sep=' '))))
    input_list.sort()

    recur_print(input_list, 0, output_len)

    return


if __name__ == "__main__":
    main()
