import sys


def recur_print(input_count, start_index, output_len, print_str='') -> None:
    if output_len == 0:
        print(print_str)
        return

    for temp_index, temp_val in enumerate(input_count[start_index:]):
        if temp_val[1] == 0:
            continue

        input_count[start_index + temp_index][1] -= 1
        recur_print(input_count, start_index + temp_index, output_len - 1, print_str + "{0} ".format(temp_val[0]))
        input_count[start_index + temp_index][1] += 1

    return


def main() -> None:
    input_len, output_len = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))

    input_list.sort()

    input_count = [[input_list[0], 1]]
    for temp_int in input_list[1:]:
        if temp_int == input_count[-1][0]:
            input_count[-1][1] += 1
        else:
            input_count.append([temp_int, 1])

    recur_print(input_count, 0, output_len)

    return


if __name__ == "__main__":
    main()
