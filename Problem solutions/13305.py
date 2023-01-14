import sys


input_len = int(sys.stdin.readline().rstrip())
dist_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
oil_cost_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))


min_oil_cost = oil_cost_arr[0]
output_num = dist_arr[0] * min_oil_cost
for temp_index in range(1, input_len - 1):
    min_oil_cost = min(min_oil_cost, oil_cost_arr[temp_index])
    output_num += dist_arr[temp_index] * min_oil_cost


print(output_num)
