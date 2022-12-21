import sys


P_num = int(sys.stdin.readline().rstrip())
str_len = int(sys.stdin.readline().rstrip())
str_arr = sys.stdin.readline().rstrip()

# result number(sub-string number)
output_num = 0
# temp number of "IO" sub-string and temp index position for str_arr
temp_num = temp_index = 0
# loop through the full string
while temp_index < str_len:
    # if the next sub-string is "IO"
    if temp_index + 1 < str_len and str_arr[temp_index:temp_index + 2] == "IO":
        # add 1 to the output sub-string
        temp_num += 1
        # add 1 to the index count making the loop skip the "IO" at once
        temp_index += 1
    # if the next sub-string is not "IO"
    else:
        # if the next char is 'I' then we evaluate the output with "~IOI" ending in mind
        if str_arr[temp_index] == 'I' and temp_num >= P_num:
            output_num += temp_num - P_num + 1
        # if the next char is 'O' then we evaluate the output with "~IOO" ending in mind
        if str_arr[temp_index] == 'O' and temp_num >= P_num:
            # Ex "IOIOIOO": Here the temp_num is 3 because there are 3 "IO"s
            # there are 2 "IOI"s in this string making the output_num += 2
            output_num += temp_num - P_num
        # if the next sub-string is not "IO" set "IO" count to 0
        temp_num = 0
    # add 1 to index
    temp_index += 1
# if the string ends with a "IO" chain
if temp_num >= P_num:
    # Ex "IOIOIO": Here the temp_num is 3 because there are 3 "IO"s
    # there are 2 "IOI"s in this string making the output_num += 2
    output_num += temp_num - P_num
print(output_num)
