import sys
from collections import deque


def main():
    input_len = int(sys.stdin.readline().rstrip())
    input_list = sys.stdin.readline().rstrip().split(sep=' ')
    max_output_list = []
    max_stack = deque([9])
    max_num = 8
    min_output_list = []
    min_stack = deque([0])
    min_num = 1

    for temp_char in input_list:
        if temp_char == '>':
            while max_stack:
                max_output_list.append(max_stack.pop())
        else:
            while min_stack:
                min_output_list.append(min_stack.pop())
        max_stack.append(max_num)
        min_stack.append(min_num)
        max_num -= 1
        min_num += 1

    while max_stack:
        max_output_list.append(max_stack.pop())
    while min_stack:
        min_output_list.append(min_stack.pop())

    print(''.join(map(str, max_output_list)))
    print(''.join(map(str, min_output_list)))

    return


if __name__ == '__main__':
    main()
