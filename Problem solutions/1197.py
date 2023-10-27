from collections import defaultdict
import sys


def parent_find(input_node, parent_list):
    if input_node == parent_list[input_node]:
        return input_node
    return parent_find(parent_list[input_node], parent_list)


def main() -> None:
    node_num, line_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    line_list = [list(map(int, sys.stdin.readline().rstrip().split(sep=' '))) for _ in range(line_num)]

    line_list.sort(key=lambda x: x[2])

    parent_list = [i for i in range(node_num + 1)]

    output_num = 0

    for start_node, end_node, line_weight in line_list:
        start_parent = parent_find(start_node, parent_list)
        end_parent = parent_find(end_node, parent_list)

        if start_parent == end_parent:
            continue

        if start_parent > end_parent:
            parent_list[start_parent] = end_parent
        else:
            parent_list[end_parent] = start_parent

        output_num += line_weight

    print(output_num)


if __name__ == '__main__':
    main()
