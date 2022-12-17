import sys


R = 31
M = 1234567891


_ = int(sys.stdin.readline().rstrip())
input_str = sys.stdin.readline().rstrip()
output_num = 0


for temp_index, temp_str in enumerate(input_str):
    output_num += (ord(temp_str) - 96) * (R ** temp_index)
    output_num %= M


print(output_num)
