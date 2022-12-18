import sys


test_num = int(sys.stdin.readline().rstrip())
check_arr = [0 for _ in range(10)]
check_arr[0] = 1
check_arr[1] = 2
check_arr[2] = 4
temp_index = 3
while temp_index < 10:
    check_arr[temp_index] = check_arr[temp_index - 1] + check_arr[temp_index - 2] + check_arr[temp_index - 3]
    temp_index += 1
for _ in range(test_num):
    print(check_arr[int(sys.stdin.readline().rstrip()) - 1])