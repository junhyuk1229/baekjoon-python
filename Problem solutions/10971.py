import sys, math


def recur_visit(input_map: list, check_list: list, left_num: int, last_index: int, start_index: int, comp_num=0):
    if left_num == 0:
        if input_map[last_index][start_index] == 0:
            return math.inf
        return comp_num + input_map[last_index][start_index]

    output_num = math.inf
    for temp_index, temp_val in enumerate(check_list):
        if temp_val or input_map[last_index][temp_index] == 0:
            continue
        check_list[temp_index] = True
        max_check = recur_visit(input_map, check_list, left_num - 1, temp_index, start_index,
                                comp_num + input_map[last_index][temp_index])
        output_num = min(output_num, max_check)
        check_list[temp_index] = False

    return output_num


def start_recur(input_map: list, check_list: list) -> int:
    left_num = len(input_map)
    output_num = math.inf
    for start_index in range(left_num):
        check_list[start_index] = True
        comp_num = recur_visit(input_map, check_list, left_num - 1, start_index, start_index)
        output_num = min(output_num, comp_num)
        check_list[start_index] = False

    return output_num


def main() -> None:
    input_len = int(sys.stdin.readline().rstrip())
    input_map = [list(map(int, sys.stdin.readline().rstrip().split(sep=' '))) for _ in range(input_len)]

    check_list = [False] * input_len

    print(start_recur(input_map, check_list))

    return


if __name__ == "__main__":
    main()
