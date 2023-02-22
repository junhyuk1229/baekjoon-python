import sys


def recur_print(input_list, output_num, print_str=""):
    if output_num == 0:
        print(print_str)
        return
    for temp_char in input_list:
        recur_print(input_list, output_num - 1, print_str + "{0} ".format(temp_char))
    return


def main() -> None:
    input_num, output_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    input_list.sort()

    recur_print(input_list, output_num)

    return


if __name__ == "__main__":
    main()
