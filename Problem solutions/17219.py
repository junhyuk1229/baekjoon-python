import sys


input_num, output_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
input_dict = dict()
for _ in range(input_num):
    temp_key, temp_value = sys.stdin.readline().rstrip().split(sep=' ')
    input_dict[temp_key] = temp_value
for _ in range(output_num):
    temp_key = sys.stdin.readline().rstrip()
    print(input_dict[temp_key])