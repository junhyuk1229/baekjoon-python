import sys


input_num = int(sys.stdin.readline().rstrip())
input_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
check_arr = dict()
output_num = 0

for temp_input in input_arr:
    temp_num = 1
    for t_temp_key, t_temp_value in check_arr.items():
        if t_temp_key >= temp_input or t_temp_value < temp_num:
            continue
        temp_num = t_temp_value + 1
    check_arr.update({temp_input: temp_num})
    if output_num > temp_num:
        continue
    output_num = temp_num

print(output_num)
