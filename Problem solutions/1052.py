import sys
from collections import deque


def main():
    water_num, goal_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    index_deque = deque()
    index_num = 0
    while water_num:
        if water_num % 2:
            index_deque.append(index_num)
        index_num += 1
        water_num //= 2
    output_num = 0
    while len(index_deque) > goal_num:
        first_index = index_deque.popleft()
        second_index = index_deque.popleft()
        output_num += pow(2, second_index) - pow(2, first_index)
        index_deque.appendleft(second_index + 1)
    print(output_num)
    return


if __name__ == '__main__':
    main()
