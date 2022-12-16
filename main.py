import sys


y, x, block_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
input_arr = []
max_num = 0
min_num = 256
for temp_index in range(y):
    input_arr.append(list(map(int, sys.stdin.readline().rstrip().split(sep=' '))))
    max_num = max(max_num, max(input_arr[temp_index]))
for sum_num in range(min_num, max_num + 1):
    remove_num = 0
    add_num = 0
