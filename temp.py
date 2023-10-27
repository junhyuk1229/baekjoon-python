import sys


def find_root(check_list, node_num):
    temp_num = node_num

    while check_list[temp_num] != temp_num:
        temp_num = check_list[temp_num]

    return temp_num


def main() -> None:
    node_num, op_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    check_list = [index_num for index_num in range(node_num)]

    print(check_list)

    for _ in range(op_num):
        temp_op, from_node, to_node = map(int, sys.stdin.readline().rstrip().split(sep=' '))

        from_node -= 1
        to_node -= 1

        if temp_op == 0:
            while from_node != check_list[from_node]:
                temp_node = check_list[from_node]

                check_list[from_node] = to_node

                from_node = temp_node

            check_list[from_node] = to_node

        else:
            if find_root(check_list, from_node) == find_root(check_list, to_node):
                print("YES")

            else:
                print("NO")

    print(check_list)

    return


if __name__ == '__main__':
    main()
