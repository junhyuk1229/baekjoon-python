import sys


input_str = sys.stdin.readline().rstrip()
output_arr = []
for temp_index in range(len(input_str)):
    output_arr.append(input_str[temp_index:])
output_arr.sort()
print('\n'.join(output_arr))
