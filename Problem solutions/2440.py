import sys


level_num = int(sys.stdin.readline())


for temp_num in range(level_num, 0, -1):
    for _ in range(temp_num):
        print("*", end='')
    print()
