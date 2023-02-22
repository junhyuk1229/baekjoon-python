import sys, math


def recur_road(input_map, check_list, check_num, output_list=[]):
    if check_num == 0:
        output_num = input_map[output_list[-1]][output_list[0]]

        if output_num == 0:
            return math.inf

        for temp_index, temp_val in enumerate(output_list[1:]):
            if input_map[output_list[temp_index]][temp_val] == 0:
                return math.inf

            output_num += input_map[output_list[temp_index]][temp_val]

        return output_num

    output_num = math.inf
    for temp_index, temp_val in enumerate(check_list):
        if temp_val:
            continue

        check_list[temp_index] = True
        output_list.append(temp_index)
        comp_num = recur_road(input_map, check_list, check_num - 1, output_list)
        output_list.pop()
        check_list[temp_index] = False

        output_num = min(output_num, comp_num)

    return output_num


def main() -> None:
    input_len = int(sys.stdin.readline().rstrip())
    input_map = [list(map(int, sys.stdin.readline().rstrip().split(sep=' '))) for _ in range(input_len)]

    check_list = [False] * input_len

    print(recur_road(input_map, check_list, input_len))

    return


if __name__ == "__main__":
    main()
