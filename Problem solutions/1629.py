import sys


num_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
output_num = 1
num_arr[0] %= num_arr[2]
while num_arr[1] > 0:
    if num_arr[1] % 2 == 1:
        output_num *= num_arr[0]
        output_num %= num_arr[2]
    num_arr[1] //= 2
    num_arr[0] *= num_arr[0]
    num_arr[0] %= num_arr[2]


print(output_num)
