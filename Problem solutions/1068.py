import sys
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.child = []


class Tree:
    def __init__(self):
        self.root = []


tree_size = int(sys.stdin.readline().rstrip())
input_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
node_delete = int(sys.stdin.readline().rstrip())


tree_arr = []
root_arr = []
for _ in range(tree_size):
    tree_arr.append(Node(0))
for temp_node, parent_num in zip(tree_arr, input_arr):
    if parent_num == -1:
        root_arr.append(temp_node)
    else:
        tree_arr[parent_num].child.append(temp_node)
delete_parent = input_arr[node_delete]
if delete_parent == -1:
    root_arr.remove(tree_arr[node_delete])
else:
    tree_arr[input_arr[node_delete]].child.remove(tree_arr[node_delete])
leaf_num = 0
temp_queue = deque(root_arr)
while temp_queue:
    temp_node = temp_queue.pop()
    if len(temp_node.child) == 0:
        leaf_num += 1
    else:
        for temp_child in temp_node.child:
            temp_queue.append(temp_child)
print(leaf_num)
