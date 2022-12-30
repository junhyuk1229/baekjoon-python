import sys


input_num = int(sys.stdin.readline().rstrip())
prev_prev_num = 0
prev_num = 1
curr_num = 1


for _ in range(input_num - 2):
    prev_prev_num = prev_num
    prev_num = curr_num
    curr_num = prev_prev_num + prev_num


print(curr_num)
