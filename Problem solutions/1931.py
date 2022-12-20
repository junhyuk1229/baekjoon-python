import sys


input_num = int(sys.stdin.readline())
input_arr = []
for _ in range(input_num):
    input_arr.append(list(map(int, sys.stdin.readline().rstrip().split(sep=' '))))

input_arr.sort(key=lambda x: x[0])
input_arr.sort(key=lambda x: x[1])

temp_time = 0
output_num = 0

for temp_arr in input_arr:
    if temp_time <= temp_arr[0]:
        temp_time = temp_arr[1]
        output_num += 1

print(output_num)
