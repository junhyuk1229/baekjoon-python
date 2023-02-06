import sys, math, heapq


def main():
    node_num, line_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    start_index = int(sys.stdin.readline().rstrip()) - 1
    input_map = [[] for _ in range(node_num)]
    for _ in range(line_num):
        from_node, to_node, line_val = map(int, sys.stdin.readline().rstrip().split(sep=' '))
        input_map[from_node - 1].append([to_node - 1, line_val])
    output_list = [math.inf] * node_num

    queue_list = []
    heapq.heappush(queue_list, (0, start_index))

    while queue_list:
        dist_val, to_node = heapq.heappop(queue_list)
        if output_list[to_node] != math.inf:
            continue
        output_list[to_node] = dist_val
        for temp_node in input_map[to_node]:
            if output_list[temp_node[0]] != math.inf:
                continue
            heapq.heappush(queue_list, (dist_val + temp_node[1], temp_node[0]))

    for temp_num in output_list:
        if temp_num != math.inf:
            print(temp_num)
            continue
        print("INF")

    return


if __name__ == "__main__":
    main()
