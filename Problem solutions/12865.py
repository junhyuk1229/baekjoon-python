import sys


input_num, weight_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
input_arr = [0] * (weight_num + 1)


for _ in range(input_num):
    temp_weight, temp_point = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    output_arr = input_arr[:]
    for temp_index in range(weight_num - temp_weight + 1):
        output_arr[temp_weight + temp_index] = max(input_arr[temp_weight + temp_index], input_arr[temp_index] + temp_point)
    input_arr = output_arr

print(max(input_arr))
