import sys


def main() -> None:
    list_length, inst_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    output_list = [i for i in range(1, list_length + 1)]

    for i in range(inst_num):
        start_index, end_index = map(int, sys.stdin.readline().rstrip().split(sep=' '))
        start_index -= 1
        end_index -= 1

        changed_list = output_list[start_index:end_index + 1][::-1]

        for index, value in enumerate(changed_list):
            output_list[start_index + index] = value

    print(' '.join(map(str, output_list)))


if __name__ == '__main__':
    main()
