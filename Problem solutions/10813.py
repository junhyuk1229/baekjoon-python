import sys


def main() -> None:
    list_len, case_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    output_list = [i + 1 for i in range(list_len)]

    for _ in range(case_num):
        a_index, b_index = map(int, sys.stdin.readline().rstrip().split(sep=' '))

        a_index -= 1
        b_index -= 1

        output_list[a_index], output_list[b_index] = output_list[b_index], output_list[a_index]

    print(' '.join(map(str, output_list)))


if __name__ == '__main__':
    main()
