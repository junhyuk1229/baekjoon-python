import sys


line_num = int(sys.stdin.readline().rstrip())
for _ in range(line_num):
    input_arr = list(sys.stdin.readline().rstrip().split(sep=' '))
    for temp_str in input_arr:
        print(temp_str[::-1], end=' ')
    print()
