import sys


input_num, base_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
output_list = []
if input_num == 0:
    output_list.append(0)


while input_num:
    output_list.append(input_num % base_num)
    input_num //= base_num


for temp_num in output_list[::-1]:
    if temp_num >= 10:
        temp_num = chr(ord('A') + temp_num - 10)
    print(temp_num, end='')
