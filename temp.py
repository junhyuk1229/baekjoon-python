import sys


def sum_list(input_list: list, sum_num: int) -> None:
    for temp_index in range(len(input_list) - 1):
        input_list[temp_index] += sum_num
    return


def sub_list(input_list: list, sub_num: int) -> None:
    for temp_index in range(len(input_list) - 1):
        input_list[temp_index] -= sub_num
    return


def check_list(input_map: list, check_list: list, check_len: int) -> bool:
    # check if check_list matches with the input_map
    for temp_index in range(check_len - 1):
        if check_list[temp_index] >= 0 and input_map[temp_index][check_len - 1] == '-':
            return False
        if check_list[temp_index] == 0 and input_map[temp_index][check_len - 1] == '0':
            return False
        if check_list[temp_index] <= 0 and input_map[temp_index][check_len - 1] == '+':
            return False
    return True


def loop_comb_num(input_map: list, input_list: list, output_list: list, start_index=0) -> bool:
    if start_index == len(input_list):
        return True

    if input_list[start_index] == '-':
        for temp_num in range(-1, -11, -1):
            output_list.append(temp_num)
            if loop_comb_num(input_map, input_list, output_list, start_index + 1):
                return True
            output_list.pop()
    elif input_list[start_index] == '0':
        output_list.append(0)
        if loop_comb_num(input_map, input_list, output_list, start_index + 1):
            return True
        output_list.pop()
    else:
        for temp_num in range(1, 11):
            output_list.append(temp_num)
            if loop_comb_num(input_map, input_list, output_list, start_index + 1):
                return True
            output_list.pop()

    return False


def main() -> None:
    input_size = int(sys.stdin.readline().rstrip())
    temp_input = sys.stdin.readline().rstrip()
    input_map = []
    start_index = 0
    for temp_d in range(input_size, 0, -1):
        input_map.append(' ' * (input_size - temp_d) + temp_input[start_index:start_index + temp_d])
        start_index += temp_d
    # print(input_map)

    input_list = [input_map[temp_index][temp_index] for temp_index in range(input_size)]
    output_list = []
    loop_comb_num(input_map, input_list, output_list)

    print(' '.join(map(str, output_list)))

    return


if __name__ == '__main__':
    main()
