import sys


def print_pattern(input_num: int) -> list:
    if input_num == 3:
        return ['***', '* *', '***']
    result_arr = []
    input_num //= 3
    temp_arr = print_pattern(input_num)
    for temp_str in temp_arr:
        result_arr.append(temp_str * 3)
    for temp_str in temp_arr:
        result_arr.append(temp_str + ' ' * len(temp_str) + temp_str)
    for temp_str in temp_arr:
        result_arr.append(temp_str * 3)
    return result_arr


input_num = int(sys.stdin.readline().rstrip())
for temp_str in print_pattern(input_num):
    print(temp_str)
