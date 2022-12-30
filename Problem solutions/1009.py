import sys


case_num = int(sys.stdin.readline().rstrip())


for _ in range(case_num):
    output_num = 1
    input_num, power_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    input_num %= 10
    while power_num != 0:
        if power_num % 2 == 1:
            output_num *= input_num
            output_num %= 10
        power_num //= 2
        input_num *= input_num
        input_num %= 10
    if output_num == 0:
        output_num = 10
    print(output_num)
