import sys, math


min_output = math.inf


def loop_check(shop_arr, house_arr, shop_index, left_num, sum_arr):
    if left_num == 0:
        global min_output
        min_output = min(min_output, sum(sum_arr))
        return
    for temp_index in range(shop_index, len(shop_arr) - left_num + 1):
        temp_arr = sum_arr.copy()
        for house_index, temp_house in enumerate(house_arr):
            temp_dist = abs(temp_house[0] - shop_arr[temp_index][0]) + abs(temp_house[1] - shop_arr[temp_index][1])
            temp_arr[house_index] = min(temp_arr[house_index], temp_dist)
        loop_check(shop_arr, house_arr, temp_index + 1, left_num - 1, temp_arr)
    return


map_size, shop_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
shop_arr = []
house_arr = []


for temp_x in range(map_size):
    input_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    for temp_y, value in enumerate(input_arr):
        if value == 1:
            house_arr.append([temp_x, temp_y])
        elif value == 2:
            shop_arr.append([temp_x, temp_y])


sum_arr = [math.inf] * len(house_arr)
loop_check(shop_arr, house_arr, 0, shop_num, sum_arr)
print(min_output)
