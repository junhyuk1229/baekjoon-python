import sys


week_num = int(sys.stdin.readline().rstrip())
point_arr = [0] * (week_num + 1)


for temp_index in range(week_num):
    input_time, input_money = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    if temp_index != 0:
        point_arr[temp_index] = max(point_arr[temp_index], point_arr[temp_index - 1])
    end_time = temp_index + input_time
    if end_time > week_num:
        continue
    check_max = point_arr[temp_index] + input_money
    point_arr[end_time] = max(point_arr[end_time], check_max)
point_arr[-1] = max(point_arr[-1], point_arr[-2])


print(point_arr[-1])
