import sys


input_len = int(sys.stdin.readline().rstrip())
input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
acc_list = [1] * input_len
dec_list = [1] * input_len


for temp_index in range(1, input_len):
    max_num = 0
    for comp_index in range(temp_index):
        if input_list[comp_index] >= input_list[temp_index]:
            continue
        max_num = max(max_num, acc_list[comp_index])
    acc_list[temp_index] = max_num + 1


for temp_index in range(input_len - 2, -1, -1):
    max_num = 0
    for comp_index in range(temp_index + 1, input_len):
        if input_list[comp_index] >= input_list[temp_index]:
            continue
        max_num = max(max_num, dec_list[comp_index])
    dec_list[temp_index] = max_num + 1


max_num = 0
for acc_num, dec_num in zip(acc_list, dec_list):
    max_num = max(max_num, acc_num + dec_num - 1)


print(max_num)
