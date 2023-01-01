import sys, math


class_num = int(sys.stdin.readline().rstrip())
class_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
main_num, sub_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
output_num = 0


for temp_num in class_arr:
    output_num += 1
    if temp_num <= main_num:
        continue
    output_num += math.ceil((temp_num - main_num) / sub_num)


print(output_num)
