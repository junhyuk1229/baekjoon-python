import sys


def gcd(first_num, second_num):
    if first_num < second_num:
        first_num, second_num = second_num, first_num
    while second_num != 0:
        temp_num = first_num % second_num
        first_num = second_num
        second_num = temp_num
    return first_num


case_num = int(sys.stdin.readline().rstrip())
for _ in range(case_num):
    M, N, x, y = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    start_num = y
    gcd_mn = gcd(M, N)
    while start_num <= M * N / gcd_mn:
        if (start_num - 1) % M + 1 == x:
            break
        start_num += N
    if start_num > M * N / gcd_mn:
        start_num = -1
    print(start_num)
