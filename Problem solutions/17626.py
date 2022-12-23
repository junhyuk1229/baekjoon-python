import sys
import math

# saves the min amount of numbers needed to get answer
output_num = 5


def i(curr_num, remainder_num):
    # if the remainder number is 0 then we found an answer so check the length
    if remainder_num == 0:
        global output_num
        # save the smallest length
        if output_num > curr_num:
            output_num = curr_num
        return
    # if the remainder is not 0 and there are 4 numbers in the list go back
    if curr_num == 4:
        return
    # loop through the possible numbers
    pos_max_num = math.floor(math.sqrt(remainder_num))
    pos_min_num = math.ceil(math.sqrt(remainder_num / (4 - curr_num)))
    for temp_num in range(pos_min_num, pos_max_num + 1):
        i(curr_num + 1, remainder_num - temp_num ** 2)


# number that was inputted
input_num = int(sys.stdin.readline().rstrip())
# loop through the list to find correct list of numbers
i(0, input_num)
# print output
print(output_num)
