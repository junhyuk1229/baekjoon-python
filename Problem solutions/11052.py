import sys


input_num = int(sys.stdin.readline().rstrip())
input_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
output_arr = input_arr.copy()


for temp_index, temp_num in enumerate(input_arr):
    for add_index in range(input_num - temp_index - 1):
        comp_num = temp_num + output_arr[add_index]
        output_arr[add_index + temp_index + 1] = max(comp_num, output_arr[add_index + temp_index + 1])


print(output_arr[-1])
