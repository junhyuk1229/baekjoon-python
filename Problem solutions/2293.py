import sys


coin_num, total_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
coin_arr = [0] * (total_num + 1)
coin_arr[0] = 1


for _ in range(coin_num):
    input_num = int(sys.stdin.readline().rstrip())
    for temp_index in range(total_num - input_num + 1):
        coin_arr[temp_index + input_num] += coin_arr[temp_index]


print(coin_arr[total_num])
