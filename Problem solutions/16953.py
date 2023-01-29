from collections import deque
import sys


def dfs(input_queue, min_num):
    output_queue = deque()
    while input_queue:
        temp_num = input_queue.pop()
        if temp_num % 10 == 1 and temp_num // 10 >= min_num:
            output_queue.append(temp_num // 10)
        if temp_num % 2 == 0 and temp_num // 2 >= min_num:
            output_queue.append(temp_num // 2)
    return output_queue


def main():
    end_num, start_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    output_num = 1
    temp_queue = deque([start_num])
    while temp_queue:
        temp_queue = dfs(temp_queue, end_num)
        output_num += 1
        if end_num in temp_queue:
            print(output_num)
            return
    print(-1)
    return


if __name__ == "__main__":
    main()
