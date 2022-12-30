import sys


arr_len, add_index = map(int, sys.stdin.readline().rstrip().split(sep=' '))
temp_index = -1
input_arr = [temp_num + 1 for temp_num in range(arr_len)]
output_arr = []


while input_arr:
    temp_index += add_index
    temp_index %= len(input_arr)
    output_arr.append(input_arr.pop(temp_index))
    temp_index -= 1


print(f"<{', '.join(map(str, output_arr))}>")
