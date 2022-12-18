import sys


instruct_num = int(sys.stdin.readline().rstrip())
check_arr = [0 for _ in range(20)]
for _ in range(instruct_num):
    input_arr = list(sys.stdin.readline().rstrip().split(sep=' '))
    if input_arr[0] == "add":
        check_arr[int(input_arr[1]) - 1] = 1
    elif input_arr[0] == "remove":
        check_arr[int(input_arr[1]) - 1] = 0
    elif input_arr[0] == "check":
        print(check_arr[int(input_arr[1]) - 1])
    elif input_arr[0] == "toggle":
        check_arr[int(input_arr[1]) - 1] ^= 1
    elif input_arr[0] == "all":
        check_arr = [1 for _ in range(20)]
    else:
        check_arr = [0 for _ in range(20)]
