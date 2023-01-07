import sys


input_str = sys.stdin.readline().rstrip()
curr_rod = 0
output_num = 0
first_minus = False
for temp_char in input_str:
    if temp_char == '(':
        curr_rod += 1
        first_minus = True
    if temp_char == ')':
        curr_rod -= 1
        if first_minus:
            output_num += curr_rod
        else:
            output_num += 1
        first_minus = False

print(output_num)
