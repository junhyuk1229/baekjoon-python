import sys


start_str = list(sys.stdin.readline().rstrip())
cursor_pos = len(start_str)
instruct_num = int(sys.stdin.readline().rstrip())

for _ in range(instruct_num):
    temp_instruct = list(sys.stdin.readline().rstrip().split(sep=' '))
    if temp_instruct[0] == 'P':
        start_str.insert(cursor_pos, temp_instruct[1])
        cursor_pos += 1
    elif temp_instruct[0] == 'L':
        if cursor_pos == 0:
            continue
        cursor_pos -= 1
    elif temp_instruct[0] == 'D':
        if cursor_pos == len(start_str):
            continue
        cursor_pos += 1
    else:
        if cursor_pos == 0:
            continue
        start_str.pop(cursor_pos - 1)
        cursor_pos -= 1

for temp_char in start_str:
    print(temp_char, end='')
