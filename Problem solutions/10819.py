import sys


def print_all_comb(input_list, check_list, left_num, check_num=0, last_num=0):
    if left_num == 0:
        return check_num

    output_num = 0
    for temp_index, temp_val in enumerate(input_list):
        if check_list[temp_index]:
            continue
        check_list[temp_index] = True
        if left_num == len(input_list):
            comp_num = print_all_comb(input_list, check_list, left_num - 1, check_num, temp_val)
        else:
            comp_num = print_all_comb(input_list, check_list, left_num - 1, check_num + abs(last_num - temp_val), temp_val)
        output_num = max(output_num, comp_num)
        check_list[temp_index] = False

    return output_num


def main() -> None:
    input_num = int(sys.stdin.readline().rstrip())
    input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))

    check_list = [False] * input_num

    print(print_all_comb(input_list, check_list, input_num))

    return


if __name__ == "__main__":
    main()
