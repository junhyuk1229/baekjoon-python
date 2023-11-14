from collections import deque
import sys


def search_dfs(curr_node: int, input_map: list, check_list: list, left_num: int = 4) -> bool:
    if left_num == 0:
        return True

    for check_num in input_map[curr_node]:
        if curr_node == check_num or check_list[check_num]:
            continue

        check_list[check_num] = True

        if search_dfs(check_num, input_map, check_list, left_num - 1):
            return True

        check_list[check_num] = False

    return False


def main() -> None:
    map_size, relation_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    input_map = [[] for _ in range(map_size)]
    for _ in range(relation_num):
        from_node, to_node = map(int, sys.stdin.readline().rstrip().split(sep=' '))
        input_map[from_node].append(to_node)
        input_map[to_node].append(from_node)

    for temp_node in range(map_size):
        check_list = [False] * map_size

        check_list[temp_node] = True

        if search_dfs(temp_node, input_map, check_list):
            print(1)
            return

    print(0)

    return


if __name__ == "__main__":
    main()
