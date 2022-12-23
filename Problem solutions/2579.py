import sys


stair_num = int(sys.stdin.readline().rstrip())
# stores prev prev max number
prev_prev_max = 0
# stores prev arr
prev_arr = [0, 0]

for _ in range(stair_num):
    input_num = int(sys.stdin.readline().rstrip())
    next_prev_arr = [prev_arr[1] + input_num, prev_prev_max + input_num]
    prev_prev_max = max(prev_arr)
    prev_arr = next_prev_arr

print(max(prev_arr))
