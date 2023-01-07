import sys


input_str = sys.stdin.readline()
while input_str:
    output_str = [0] * 4
    for temp_char in input_str:
        if temp_char.islower():
            output_str[0] += 1
        if temp_char.isupper():
            output_str[1] += 1
        if temp_char.isdigit():
            output_str[2] += 1
        elif temp_char == ' ':
            output_str[3] += 1
    print(' '.join(map(str, output_str)))
    input_str = sys.stdin.readline()
