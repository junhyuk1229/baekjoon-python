import sys


stair_arr = [1] * 10
stair_arr[0] = 0
stair_num = int(sys.stdin.readline().rstrip())


for _ in range(stair_num - 1):
    temp_arr = [0] * 10
    for temp_index in range(10):
        if temp_index != 0:
            temp_arr[temp_index - 1] += stair_arr[temp_index]
        if temp_index != 9:
            temp_arr[temp_index + 1] += stair_arr[temp_index]
    stair_arr = temp_arr


print(sum(stair_arr) % 1000000000)
