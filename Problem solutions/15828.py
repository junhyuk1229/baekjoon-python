import sys
from collections import deque


def main():
    buffer_max_len = int(sys.stdin.readline().rstrip())
    buffer_arr = deque()
    buffer_len = 0
    input_num = int(sys.stdin.readline().rstrip())
    while input_num != -1:
        if input_num == 0:
            buffer_arr.popleft()
            buffer_len -= 1
        else:
            if buffer_len < buffer_max_len:
                buffer_arr.append(input_num)
                buffer_len += 1
        input_num = int(sys.stdin.readline().rstrip())
    if buffer_len == 0:
        print("empty")
    else:
        print(' '.join(map(str, buffer_arr)))


if __name__ == "__main__":
    main()
