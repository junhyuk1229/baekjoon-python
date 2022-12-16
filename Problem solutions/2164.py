import sys
from collections import deque


def main():
    input_len = int(sys.stdin.readline().rstrip())
    input_arr = deque()
    for i in range(input_len):
        input_arr.append(i + 1)
    for _ in range(input_len - 1):
        input_arr.popleft()
        temp_num = input_arr.popleft()
        input_arr.append(temp_num)
    print(input_arr[0])


if __name__ == "__main__":
    main()
