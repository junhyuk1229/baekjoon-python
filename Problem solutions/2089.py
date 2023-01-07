import sys


input_num = int(sys.stdin.readline().rstrip())
output_arr = []
temp_char = 1
if input_num == 0:
    output_arr.append('0')


while input_num:
    if input_num % (2 * temp_char):
        input_num -= temp_char
        output_arr.append('1')
    else:
        output_arr.append('0')
    temp_char *= -2


print(''.join(output_arr[::-1]))
