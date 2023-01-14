import sys


input_arr_len, sum_len = map(int, sys.stdin.readline().rstrip().split(sep=' '))
input_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))


comp_sum = 0
for temp_index in range(sum_len):
    comp_sum += input_arr[temp_index]


output_max = comp_sum
for comp_index in range(input_arr_len - sum_len):
    comp_sum += input_arr[comp_index + sum_len] - input_arr[comp_index]
    output_max = max(output_max, comp_sum)


print(output_max)
