import sys


input_base, output_base = map(int, sys.stdin.readline().rstrip().split(sep=' '))
input_len = int(sys.stdin.readline().rstrip())
input_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))

# convert from input base to decimal
check_num = 0
for temp_num in input_arr:
    check_num *= input_base
    check_num += temp_num

# convert from decimal to output base
output_arr = []
while check_num:
    output_arr.append(check_num % output_base)
    check_num //= output_base


print(' '.join(map(str, output_arr[::-1])))
