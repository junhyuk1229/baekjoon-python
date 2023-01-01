import sys, math


city_num = int(sys.stdin.readline().rstrip())
conn_num = int(sys.stdin.readline().rstrip())
conn_map = [[math.inf] * (city_num + 1) for _ in range(city_num + 1)]
for _ in range(conn_num):
    from_city, to_city, input_time = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    conn_map[from_city][to_city] = min(input_time, conn_map[from_city][to_city])
from_city, to_city = map(int, sys.stdin.readline().rstrip().split(sep=' '))
check_arr = [False] * (city_num + 1)
check_arr[from_city] = True
output_arr = [math.inf] * (city_num + 1)
output_arr[from_city] = 0


while not check_arr[to_city]:
    for temp_city, temp_val in enumerate(conn_map[from_city]):
        if temp_val == math.inf or temp_city == from_city or check_arr[temp_city]:
            continue
        comp_num = temp_val + output_arr[from_city]
        output_arr[temp_city] = min(output_arr[temp_city], comp_num)
    min_val = math.inf
    min_city = -1
    for temp_city, temp_val in enumerate(output_arr):
        if min_val <= temp_val or check_arr[temp_city]:
            continue
        min_city = temp_city
        min_val = temp_val
    check_arr[min_city] = True
    from_city = min_city


print(output_arr[to_city])
