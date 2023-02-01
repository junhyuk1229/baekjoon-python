import sys, math


def main():
    node_num, line_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    start_index = int(sys.stdin.readline().rstrip()) - 1
    input_map = [[math.inf] * node_num for _ in range(node_num)]
    for _ in range(line_num):
        from_node, to_node, line_val = map(int, sys.stdin.readline().rstrip().split(sep=' '))
        input_map[from_node - 1][to_node - 1] = line_val
    output_list = [math.inf] * node_num
    check_list = [False] * node_num
    output_list[start_index] = 0

    for _ in range(node_num):
        check_list[start_index] = True
        next_index = -1
        next_min = math.inf
        for temp_index in range(node_num):
            if not check_list[temp_index] and output_list[start_index] + input_map[start_index][temp_index] < output_list[temp_index]:
                output_list[temp_index] = output_list[start_index] + input_map[start_index][temp_index]
            if next_min > check_list[temp_index]:
                next_index = temp_index
                next_min = check_list[temp_index]
        start_index = next_index

    print('\n'.join(map(str, output_list)))

    return


if __name__ == "__main__":
    main()
