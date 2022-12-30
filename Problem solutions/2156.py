import sys


input_num = int(sys.stdin.readline().rstrip())
output_max = 0
prev_list = [0, 0]

for _ in range(input_num):
    curr_arr = [int(sys.stdin.readline().rstrip())] * 2
    curr_arr[0] += output_max
    curr_arr[1] += prev_list[0]
    output_max = max(output_max, max(prev_list))
    prev_list = curr_arr

print(max(output_max, max(prev_list)))
