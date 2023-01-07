import sys


input_str, input_num = sys.stdin.readline().rstrip().split(sep=' ')
base_num = int(input_num)


output_num = 0
for temp_char in input_str:
    output_num *= base_num
    if ord('0') <= ord(temp_char) <= ord('9'):
        output_num += int(temp_char)
    else:
        output_num += ord(temp_char) - ord('A') + 10


print(output_num)
