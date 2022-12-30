import sys


MONTH_DAY = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAY_NAME = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]


month_num, day_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
curr_day = 0
for temp_month in range(month_num - 1):
    curr_day += MONTH_DAY[temp_month]
curr_day += day_num


print(DAY_NAME[curr_day % 7])
