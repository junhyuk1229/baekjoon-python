from collections import defaultdict, deque
import sys


def dfs(node_num, input_map):
    output_list = [-1] * node_num
    temp_queue = deque([0])
    while temp_queue:
        temp_index = temp_queue.pop()
        for temp_num in input_map[temp_index]:
            if output_list[temp_num] != -1:
                continue
            temp_queue.append(temp_num)
            output_list[temp_num] = temp_index + 1
    return output_list


def main():
    node_num = int(sys.stdin.readline().rstrip())
    node_map = defaultdict(list)

    for _ in range(node_num - 1):
        temp_conn = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
        node_map[temp_conn[0] - 1].append(temp_conn[1] - 1)
        node_map[temp_conn[1] - 1].append(temp_conn[0] - 1)

    print('\n'.join(map(str, dfs(node_num, node_map)[1:])))

    return


if __name__ == "__main__":
    main()
