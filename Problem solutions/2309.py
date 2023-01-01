import sys


input_arr = []
total_arr = -100
for temp_index in range(9):
    input_arr.append(int(sys.stdin.readline().rstrip()))
    total_arr += input_arr[temp_index]
input_arr.sort()
first_index = 0
second_index = 1
while True:
    if input_arr[first_index] + input_arr[second_index] == total_arr:
        break
    if input_arr[first_index] + input_arr[second_index] > total_arr:
        first_index += 1
        second_index = first_index + 1
    else:
        second_index += 1
        if second_index == 9:
            first_index += 1
            second_index = first_index + 1


for temp_index, temp_val in enumerate(input_arr):
    if temp_index == first_index or temp_index == second_index:
        continue
    print(temp_val)
