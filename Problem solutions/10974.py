import sys


def print_all_comb(check_list, left_num, print_str=''):
    if left_num == 0:
        print(print_str)
        return

    for temp_index, temp_val in enumerate(check_list):
        if temp_val:
            continue
        check_list[temp_index] = True
        print_all_comb(check_list, left_num - 1, print_str + "{0} ".format(temp_index + 1))
        check_list[temp_index] = False
    return


def main() -> None:
    input_num = int(sys.stdin.readline().rstrip())

    check_list = [False] * input_num

    print_all_comb(check_list, input_num)

    return


if __name__ == "__main__":
    main()
