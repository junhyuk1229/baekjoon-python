import sys


# (100+1+ | 01)+
# all flags will be used to check position
# 0 for next 100
# 1 for next 01
# 2 for looping 0
# 3 for looping 1


input_num = int(sys.stdin.readline().rstrip())
for _ in range(input_num):
    input_str = sys.stdin.readline().rstrip()
    check_index = 0
    flag_arr = [True, True, False, False]
    while check_index < len(input_str):
        if flag_arr[0] and check_index + 2 < len(input_str) and input_str[check_index:check_index + 3] == "100":
            check_index += 3
            flag_arr = [False, False, True, True]
        elif flag_arr[1] and check_index + 1 < len(input_str) and input_str[check_index:check_index + 2] == "01":
            check_index += 2
            flag_arr = [True, True, False, False]
        elif flag_arr[2] and input_str[check_index] == '0':
            check_index += 1
            flag_arr = [False, False, True, True]
        elif flag_arr[3] and input_str[check_index] == '1':
            check_index += 1
            flag_arr = [True, True, False, True]
        else:
            break
    if (flag_arr[0] or flag_arr[1]) and check_index == len(input_str):
        print("YES")
    else:
        print("NO")
