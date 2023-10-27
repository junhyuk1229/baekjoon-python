from collections import deque
import sys


def peek_deque(input_list: deque):
    temp_index, temp_output = input_list.pop()
    input_list.append([temp_index, temp_output])

    return temp_output


def main() -> None:
    tower_num = int(sys.stdin.readline().rstrip())

    tower_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))

    temp_deque = deque()
    output_deque = deque()

    for index, temp_tower in enumerate(tower_list[::-1]):
        while temp_deque and peek_deque(temp_deque) < temp_tower:
            temp_index, _ = temp_deque.pop()
            output_deque.append([temp_index, tower_num - index])
        temp_deque.append([index, temp_tower])

    while temp_deque:
        temp_index, _ = temp_deque.pop()
        output_deque.appendleft([temp_index, 0])

    output_list = list(output_deque)

    output_list.sort(key=lambda x: x[0], reverse=True)

    output_list = [temp_num for _, temp_num in output_list]

    print(' '.join(map(str, output_list)))


if __name__ == '__main__':
    main()
