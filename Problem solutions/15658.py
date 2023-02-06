import sys, math


OP_LIST = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: abs(x) // y]


def loop_print(input_list, sym_list, curr_index, output_num, output_list):
    if curr_index == len(input_list):
        output_list[0] = max(output_list[0], output_num)
        output_list[1] = min(output_list[1], output_num)
        return

    for temp_index in range(4):
        if sym_list[temp_index] == 0:
            continue
        temp_output_num = output_num
        sym_list[temp_index] -= 1
        output_num = OP_LIST[temp_index](output_num, input_list[curr_index])
        if temp_index == 3 and temp_output_num < 0:
            output_num = -output_num
        loop_print(input_list, sym_list, curr_index + 1, output_num, output_list)
        output_num = temp_output_num
        sym_list[temp_index] += 1
    return


def main():
    input_len = int(sys.stdin.readline().rstrip())
    input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    sym_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    output_list = [-math.inf, math.inf]

    loop_print(input_list, sym_list, 1, input_list[0], output_list)

    print('\n'.join(map(str, output_list)))

    return


if __name__ == "__main__":
    main()
