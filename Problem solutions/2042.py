import sys


MAX_LEN = 1010001


def build_tree(node_num, start_index, end_index, input_list, tree_list) -> None:
    if start_index == end_index:
        tree_list[node_num] = input_list[start_index]
        return

    mid_index = (start_index + end_index) // 2

    build_tree(node_num * 2, start_index, mid_index, input_list, tree_list)
    build_tree(node_num * 2 + 1, mid_index + 1, end_index, input_list, tree_list)

    tree_list[node_num] = tree_list[node_num * 2] + tree_list[node_num * 2 + 1]

    return


def update_tree(node_num, start_index, end_index, tree_list, index_num, add_num):
    tree_list[node_num] += add_num

    if start_index == end_index:
        return

    mid_index = (start_index + end_index) // 2

    if start_index <= index_num <= mid_index:
        update_tree(node_num * 2, start_index, mid_index, tree_list, index_num, add_num)
    else:
        update_tree(node_num * 2 + 1, mid_index + 1, end_index, tree_list, index_num, add_num)

    return


def find_tree(node_num, start_index, end_index, tree_list, first_num, end_num) -> int:
    if first_num > end_index or end_num < start_index:
        return 0

    if first_num <= start_index and end_num >= end_index:
        return tree_list[node_num]

    mid_index = (start_index + end_index) // 2

    output_num = find_tree(node_num * 2, start_index, mid_index, tree_list, first_num, end_num)
    output_num += find_tree(node_num * 2 + 1, mid_index + 1, end_index, tree_list, first_num, end_num)

    return output_num


def main() -> None:
    input_len, change_num, sum_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    input_list = [int(sys.stdin.readline().rstrip()) for _ in range(input_len)]
    tree_list = [0] * (len(input_list) * 4)

    build_tree(1, 0, len(input_list) - 1, input_list, tree_list)

    for _ in range(change_num + sum_num):
        inst_num, first_num, end_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))

        if inst_num == 1:
            index_num = first_num - 1
            add_num = end_num - input_list[index_num]
            input_list[index_num] += add_num

            update_tree(1, 0, input_len - 1, tree_list, index_num, add_num)
        else:
            first_num -= 1
            end_num -= 1

            print(find_tree(1, 0, input_len - 1, tree_list, first_num, end_num))

    return


if __name__ == "__main__":
    main()
