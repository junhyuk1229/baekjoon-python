import sys


def find_gcd(first_num, second_num):
    if first_num < second_num:
        first_num, second_num = second_num, first_num
    while second_num != 0:
        temp_num = first_num % second_num
        first_num = second_num
        second_num = temp_num
    return first_num


input_num, start_point = map(int, sys.stdin.readline().rstrip().split(sep=' '))
input_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
output_num = abs(input_arr[0] - start_point)
for temp_num in input_arr:
    output_num = find_gcd(output_num, abs(temp_num - start_point))


print(output_num)
