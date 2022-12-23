import sys


# using braces we can change all the '+' to '-' but bracing them before a '-'
# separate all the numbers by '-'
input_str = sys.stdin.readline().rstrip().split(sep='-')
print(input_str)

# used to store all the numbers that are going to be subtracted
output_arr = []
# loop through the loop to add all numbers
for temp_str in input_str:
    # saves the result of adding all number  in temp_str
    output_num = 0
    # split the numbers
    temp_arr = temp_str.split(sep='+')
    # add each element to the output_num
    for temp_num in temp_arr:
        output_num += int(temp_num)
    # add the number to the output list
    output_arr.append(output_num)
print(output_arr)

# because the first number is always positive we add the number instead of subtracting
output_num = output_arr[0]
# iterate through the array except the first element and subtract the number to the output number
for temp_num in output_arr[1:]:
    output_num -= temp_num
print(output_num)