import sys


def update(input_arr: list, input_num: int):
    while len(input_arr) < input_num:
        temp_arr = [
            (input_arr[-1][1] + input_arr[-1][2]) % 1000000009,
            (input_arr[-2][0] + input_arr[-2][2]) % 1000000009,
            (input_arr[-3][0] + input_arr[-3][1]) % 1000000009
        ]
        input_arr.append(temp_arr)
    return


case_num = int(sys.stdin.readline().rstrip())
input_arr = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]


for _ in range(case_num):
    input_num = int(sys.stdin.readline().rstrip())
    if len(input_arr) < input_num:
        update(input_arr, input_num)
    print((sum(input_arr[input_num - 1])) % 1000000009)
