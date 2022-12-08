from collections import deque
import sys


def empty(input_arr):
    if len(input_arr) == 0:
        return True
    return False


def pop(input_arr):
    if empty(input_arr):
        return -1
    return input_arr.pop()


def push(input_arr, input_char):
    input_arr.append(input_char)


def main():
    input_str = sys.stdin.readline().rstrip()
    while input_str != '.':
        check_stack = deque()
        correct_flag = True
        for temp_char in input_str:
            if temp_char == '(' or temp_char == '[':
                push(check_stack, temp_char)
            elif temp_char == ')':
                if pop(check_stack) != '(':
                    correct_flag = False
                    break
            elif temp_char == ']':
                if pop(check_stack) != '[':
                    correct_flag = False
                    break
        if correct_flag and empty(check_stack):
            print("yes")
        else:
            print("no")
        input_str = sys.stdin.readline().rstrip()


if __name__ == "__main__":
    main()
