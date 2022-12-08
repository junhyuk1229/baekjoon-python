from collections import deque
import sys


def empty(input_arr):
    if len(input_arr) == 0:
        return True
    return False


def peek(input_arr):
    if empty(input_arr):
        return 0
    temp_num = input_arr.pop()
    input_arr.append(temp_num)
    return temp_num


def pop(input_arr):
    if empty(input_arr):
        return 0
    return input_arr.pop()


def push(input_arr, input_char):
    input_arr.append(input_char)


def main():
    arr_len = int(sys.stdin.readline().rstrip())
    output_arr = deque()
    check_arr = deque()
    curr_num = 0
    temp_arr = []
    output_flag = True
    for _ in range(arr_len):
        temp_arr.append(int(sys.stdin.readline().rstrip()))
    for temp_num in temp_arr:
        if temp_num > curr_num:
            while temp_num > curr_num:
                check_arr.append(curr_num + 1)
                curr_num += 1
                output_arr.append('+')
        if peek(check_arr) == temp_num:
            pop(check_arr)
            output_arr.append('-')
        else:
            output_flag = False
            break
    if output_flag:
        print('\n'.join(output_arr))
    else:
        print("NO")


if __name__ == "__main__":
    main()
