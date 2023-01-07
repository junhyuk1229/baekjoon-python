import sys


input_str = sys.stdin.readline().rstrip()
in_bracket = False
output_arr = ''
for temp_char in input_str:
    if in_bracket:
        if temp_char == '>':
            in_bracket = False
        print(temp_char, end='')
    else:
        if temp_char in ['<', ' ']:
            if len(output_arr) != 0:
                print(output_arr[::-1], end='')
            print(temp_char, end='')
            if temp_char == '<':
                in_bracket = True
            output_arr = ''
        else:
            output_arr += temp_char


if not in_bracket and len(output_arr) != 0:
    print(output_arr[::-1])
