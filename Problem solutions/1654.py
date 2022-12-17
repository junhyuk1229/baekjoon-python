import sys, math


input_num, segment_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
input_arr = []
total_sum = 0
max_num = 0
for temp_index in range(input_num):
    input_arr.append(int(sys.stdin.readline().rstrip()))
    total_sum += input_arr[temp_index]
    max_num = max(max_num, input_arr[temp_index])
max_seg_len = math.floor(total_sum / segment_num) + 1
min_seg_len = math.floor(max_num / segment_num)
if min_seg_len == 0:
    min_seg_len = 1
while min_seg_len + 1 < max_seg_len:
    middle_seg = (max_seg_len + min_seg_len) // 2
    temp_seg = 0
    for temp_len in input_arr:
        temp_seg += temp_len // middle_seg
    if temp_seg >= segment_num:
        min_seg_len = middle_seg
    else:
        max_seg_len = middle_seg
print(min_seg_len)