import sys, math


node_num, line_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
check_node = int(sys.stdin.readline().rstrip())
map_arr = [[math.inf] * (node_num + 1) for _ in range(node_num + 1)]
for _ in range(line_num):
    from_node, to_node, val_node = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    map_arr[from_node][to_node] = min(map_arr[from_node][to_node], val_node)


output_arr = [math.inf] * (node_num + 1)
output_arr[check_node] = 0
check_arr = [False] * (node_num + 1)
for _ in range(node_num - 1):
    next_node = 0
    next_val = math.inf
    for temp_node, temp_val in enumerate(map_arr[check_node]):
        comp_num = output_arr[check_node] + temp_val
        if comp_num > output_arr[temp_node] or check_arr[temp_node]:
            continue
        if next_val > comp_num:
            next_node = temp_node
            next_val = comp_num
        output_arr[temp_node] = comp_num
    check_node = next_node
    check_arr[next_node] = True


for temp_val in output_arr[1:]:
    if temp_val == math.inf:
        print("INF")
    else:
        print(temp_val)
