import sys


def find_gcd(first_int, second_int):
    if first_int < second_int:
        first_int, second_int = second_int, first_int
    while second_int != 0:
        temp_int = first_int % second_int
        first_int = second_int
        second_int = temp_int
    return first_int


case_num = int(sys.stdin.readline().rstrip())


for _ in range(case_num):
    input_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    output_num = 0
    for first_index in range(1, input_arr[0] + 1):
        for second_index in range(first_index + 1, input_arr[0] + 1):
            output_num += find_gcd(input_arr[first_index], input_arr[second_index])
    print(output_num)
