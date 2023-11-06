import sys


MAX_NUM = 1000000001


def build_tree(node_num, start_index, end_index, input_list, tree_list) -> int:
    if start_index == end_index:
        tree_list[node_num] = input_list[start_index]
        return tree_list[node_num]

    mid_index = (start_index + end_index) // 2

    tree_list[node_num] = build_tree(node_num * 2, start_index, mid_index, input_list, tree_list)
    tree_list[node_num] = min(tree_list[node_num], build_tree(node_num * 2 + 1, mid_index + 1, end_index, input_list, tree_list))

    return tree_list[node_num]


def find_tree(node_num, start_index, end_index, tree_list, first_num, end_num) -> int:
    if first_num > end_index or end_num < start_index:
        return MAX_NUM

    if first_num <= start_index and end_num >= end_index:
        return tree_list[node_num]

    mid_index = (start_index + end_index) // 2

    output_num = find_tree(node_num * 2, start_index, mid_index, tree_list, first_num, end_num)
    output_num = min(output_num, find_tree(node_num * 2 + 1, mid_index + 1, end_index, tree_list, first_num, end_num))

    return output_num


def main() -> None:
    input_len, check_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    input_list = [int(sys.stdin.readline().rstrip()) for _ in range(input_len)]
    tree_list = [0] * (len(input_list) * 4)

    build_tree(1, 0, len(input_list) - 1, input_list, tree_list)

    for _ in range(check_num):
        first_num, end_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))

        first_num -= 1
        end_num -= 1

        print(find_tree(1, 0, input_len - 1, tree_list, first_num, end_num))

    return


if __name__ == "__main__":
    main()
