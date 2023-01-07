import sys


input_arr = sys.stdin.readline().rstrip().split(sep=' ')
first_num = int(input_arr[0] + input_arr[1])
second_num = int(input_arr[2] + input_arr[3])
print(first_num + second_num)
