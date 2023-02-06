import sys


def loop_print(input_list, start_index, output_list):
    if len(output_list) == 6:
        print(' '.join(map(str, output_list)))
        return
    for temp_index in range(start_index, len(input_list)):
        output_list.append(input_list[temp_index])
        loop_print(input_list, temp_index + 1, output_list)
        output_list.pop()
    return


def main():
    input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    while input_list[0] != 0:
        loop_print(input_list, 1, [])
        print()
        input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    return


if __name__ == "__main__":
    main()
