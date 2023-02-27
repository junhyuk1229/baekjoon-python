from collections import deque
import sys


def dfs_node(input_map: list, check_list: list, temp_deque: deque) -> bool:
    if len(temp_deque) >= 5:
        return True

    temp_node = temp_deque[-1]

    for temp_index, temp_map in enumerate(input_map[temp_node]):
        if not temp_map or check_list[temp_index]:
            continue

        temp_deque.append(temp_index)
        check_list[temp_index] = True
        if dfs_node(input_map, check_list, temp_deque):
            return True
        temp_deque.pop()
        check_list[temp_index] = False
    return False


def main() -> None:
    # Get data input + make node map
    input_num, input_len = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    input_list = [[False] * input_num for _ in range(input_num)]
    for _ in range(input_len):
        from_node, to_node = map(int, sys.stdin.readline().rstrip().split(sep=' '))
        input_list[from_node][to_node] = input_list[to_node][from_node] = True
    '''
    print(f"input_num: {input_num}")
    print(f"input_len: {input_len}")
    print("input_list:")
    for temp in input_list:
        print(temp)
    print()
    '''

    # Call dfs for each node as a starting point
    # If a path with length that is greater than 5 is found print 1

    # Set up variables
    check_list = [False] * input_num
    temp_deque = deque()
    for start_node in range(input_num):
        temp_deque.append(start_node)
        check_list[start_node] = True
        if dfs_node(input_list, check_list, temp_deque):
            print(1)
            return
        temp_deque.pop()
        check_list[start_node] = False
    print(0)

    return


if __name__ == '__main__':
    main()
