import sys


input_num = int(sys.stdin.readline().rstrip())


for temp_num in range(input_num):
    for _ in range(temp_num):
        print(" ", end='')
    for _ in range(input_num - temp_num):
        print("*", end='')
    print()
