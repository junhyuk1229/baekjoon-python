import sys


arr_len, total_cost = map(int, sys.stdin.readline().rstrip().split(sep=' '))
input_arr = []
for _ in range(arr_len):
    input_arr.append(int(sys.stdin.readline().rstrip()))
total_num = 0
input_arr = input_arr[::-1]
for temp_num in input_arr:
    total_num += total_cost // temp_num
    total_cost %= temp_num
print(total_num)
