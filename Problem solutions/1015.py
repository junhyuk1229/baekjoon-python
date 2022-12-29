import sys


input_num = int(sys.stdin.readline().rstrip())
input_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
temp_arr = list()
for temp_index, temp_value in enumerate(input_arr):
    temp_arr.append([temp_index, temp_value])
temp_arr.sort(key=lambda x: x[1])
output_arr = [0] * input_num
for temp_index, temp_value in enumerate(temp_arr):
    output_arr[temp_value[0]] = temp_index
print(' '.join(map(str, output_arr)))
