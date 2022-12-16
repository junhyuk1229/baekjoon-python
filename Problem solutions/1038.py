import sys

search_val = int(sys.stdin.readline().rstrip()) + 1
output_val = 0
temp_val = 0
index = 0
input_arr = [0]


def check_length():
    global temp_val, output_val, index
    if len(input_arr) == index:
        temp_val += 1
        if temp_val == search_val:
            output_val = ''.join(map(str, input_arr))
            return True
        if len(input_arr) == 10:
            output_val = '-1'
            return True
        return False
    if index == 0:
        end_num = 10
    else:
        end_num = input_arr[index - 1]
    for temp_num in range(len(input_arr) - index - 1, end_num):
        input_arr[index] = temp_num
        index += 1
        if check_length():
            return True
        index -= 1


while temp_val < search_val:
    if check_length():
        break
    input_arr.append(0)
    index = 0
print(output_val)