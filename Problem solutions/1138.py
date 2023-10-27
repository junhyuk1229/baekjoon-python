import sys


def main() -> None:
    list_len = int(sys.stdin.readline().rstrip())
    check_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))

    output_list = [0] * list_len

    for temp_num, shift_index in enumerate(check_list):
        temp_index = 0

        while shift_index > 0 or output_list[temp_index] != 0:
            if output_list[temp_index] == 0:
                shift_index -= 1

            temp_index += 1

        output_list[temp_index] = temp_num + 1

    print(' '.join(map(str, output_list)))

    return


if __name__ == '__main__':
    main()
