from collections import deque
import sys


def pre_print(input_dict, input_char):
    print(input_char, end='')
    if input_dict[input_char][0] != '.':
        pre_print(input_dict, input_dict[input_char][0])
    if input_dict[input_char][1] != '.':
        pre_print(input_dict, input_dict[input_char][1])


def curr_print(input_dict, input_char):
    if input_dict[input_char][0] != '.':
        curr_print(input_dict, input_dict[input_char][0])
    print(input_char, end='')
    if input_dict[input_char][1] != '.':
        curr_print(input_dict, input_dict[input_char][1])


def post_print(input_dict, input_char):
    if input_dict[input_char][0] != '.':
        post_print(input_dict, input_dict[input_char][0])
    if input_dict[input_char][1] != '.':
        post_print(input_dict, input_dict[input_char][1])
    print(input_char, end='')


def main():
    input_num = int(sys.stdin.readline().rstrip())
    input_dict = dict()
    for _ in range(input_num):
        index_char, left_char, right_char = sys.stdin.readline().rstrip().split(sep=' ')
        input_dict[index_char] = [left_char, right_char]

    pre_print(input_dict, 'A')
    print()
    curr_print(input_dict, 'A')
    print()
    post_print(input_dict, 'A')

    return


if __name__ == "__main__":
    main()
