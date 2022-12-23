import sys, math
from collections import deque


# input_queue is used to search next level
# visit_check is used to not go to nodes already visited
def bfs(conn_dict, input_queue, visit_check):
    output_queue = deque()
    while input_queue:
        temp_check_node = input_queue.pop()
        for temp_conn_node in conn_dict[temp_check_node]:
            if visit_check[temp_conn_node]:
                continue
            visit_check[temp_conn_node] = True
            output_queue.append(temp_conn_node)
    return output_queue


def check_bacon_num(conn_dict, input_node, node_num):
    visit_check = [False] * (node_num + 1)
    visit_check[input_node] = True
    input_queue = deque([input_node])
    output_num = 0
    loop_num = 0
    while input_queue:
        loop_num += 1
        input_queue = bfs(conn_dict, input_queue, visit_check)
        output_num += len(input_queue) * loop_num
    return output_num


node_num, conn_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
conn_dict = dict()
for temp_node in range(node_num):
    conn_dict[temp_node + 1] = []
for _ in range(conn_num):
    input_index, input_val = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    conn_dict[input_index].append(input_val)
    conn_dict[input_val].append(input_index)
min_num = math.inf
min_index = -1
for temp_node_num in range(1, node_num + 1):
    output_num = check_bacon_num(conn_dict, temp_node_num, node_num)
    if output_num >= min_num:
        continue
    min_num = output_num
    min_index = temp_node_num
print(min_index)
