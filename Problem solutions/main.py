import sys
from collections import deque


CONSTANTS = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']


def main():
    input_num = int(sys.stdin.readline())
    line_buffer = deque()
    constant_num = deque()
    four_const_num = 0
    for _ in range(input_num):
        input_line = sys.stdin.readline().rstrip()
        print_output = True
        temp_num = 0
        for temp_line in line_buffer:
            if temp_line == input_line:
                temp_num += 1
                if temp_num == 2:
                    print_output = False
                    break
        if print_output:
            consecutive = 0
            max_consecutive = 0
            for temp_char in input_line:
                if temp_char not in CONSTANTS and ('a' <= temp_char <= 'z' or 'A' <= temp_char <= 'Z'):
                    consecutive += 1
                else:
                    if max_consecutive < consecutive:
                        max_consecutive = consecutive
                    consecutive = 0
            if max_consecutive < consecutive:
                max_consecutive = consecutive
            if max_consecutive > 5 or (max_consecutive == 5 and four_const_num == 3):
                print_output = False
        if print_output:
            print('y')
            line_buffer.append(input_line)
            constant_num.append(max_consecutive)
            if max_consecutive == 5:
                four_const_num += 1
            if len(line_buffer) > 10:
                line_buffer.popleft()
                if constant_num.popleft() == 5:
                    four_const_num -= 1
        else:
            print('n')
    return 0


if __name__ == "__main__":
    main()
