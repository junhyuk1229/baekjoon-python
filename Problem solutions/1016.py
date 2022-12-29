import sys, math


min_num, max_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
output_arr = [1] * (max_num - min_num + 1)
output_num = max_num - min_num + 1
for temp_num in range(2, math.ceil(math.sqrt(max_num)) + 1):
    temp_start_num = (temp_num ** 2) * (math.ceil(min_num / (temp_num ** 2)))
    while temp_start_num <= max_num:
        if output_arr[temp_start_num - min_num] == 1:
            output_num -= 1
            output_arr[temp_start_num - min_num] = 0
        temp_start_num += temp_num ** 2
print(output_num)
