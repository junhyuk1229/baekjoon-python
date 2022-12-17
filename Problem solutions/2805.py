import sys, math


arr_len, tree_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
input_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))


max_tree = max(input_arr) + 1
min_tree = min(input_arr) - math.ceil(tree_num / arr_len)
while min_tree + 1 < max_tree:
    middle_tree = (max_tree + min_tree) // 2
    total_tree = 0
    for temp_tree in input_arr:
        if temp_tree > middle_tree:
            total_tree += temp_tree - middle_tree
    if total_tree >= tree_num:
        min_tree = middle_tree
    else:
        max_tree = middle_tree
print(min_tree)
