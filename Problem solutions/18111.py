import sys


height, length, inv_block = map(int, sys.stdin.readline().rstrip().split(sep=' '))
block_dict = dict()
for temp_index in range(height):
    for i in list(map(int, sys.stdin.readline().rstrip().split(sep=' '))):
        block_dict[i] = block_dict.get(i, 0) + 1
# combine both codes
floor_height = 0
min_height = 0
for temp_var in block_dict:
    floor_height = max(floor_height, temp_var)
    min_height = min(min_height, temp_var)
min_time = floor_height * height * length * 2
for temp_height in range(min_height, floor_height + 1):
    temp_time = 0
    temp_block = 0
    for temp_key, temp_value in block_dict.items():
        block_var = (temp_key - temp_height) * temp_value
        temp_block -= block_var
        if block_var > 0:
            temp_time += block_var * 2
        else:
            temp_time -= block_var
    if inv_block < temp_block:
        continue
    if min_time >= temp_time:
        min_time = temp_time
        output_height = temp_height
print(f"{min_time} {output_height}")
