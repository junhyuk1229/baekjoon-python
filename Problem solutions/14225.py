import sys
from collections import defaultdict


def recur_dict(input_dict, input_list, index_num, output_num):
    if index_num == len(input_list):
        input_dict[output_num] = True
        return

    recur_dict(input_dict, input_list, index_num + 1, output_num)
    recur_dict(input_dict, input_list, index_num + 1, output_num + input_list[index_num])
    return


def main():
    check_dict = defaultdict(lambda: False)
    _ = int(sys.stdin.readline().rstrip())
    input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))

    recur_dict(check_dict, input_list, 0, 0)

    output_num = 1
    while check_dict[output_num]:
        output_num += 1

    print(output_num)

    return


if __name__ == "__main__":
    main()
