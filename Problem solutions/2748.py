import sys


input_num = int(sys.stdin.readline().rstrip())
curr_num = 1
prev_num = 1
prev_prev_num = 0


for _ in range(input_num - 2):
    prev_prev_num = prev_num
    prev_num = curr_num
    curr_num = prev_num + prev_prev_num


print(curr_num)
