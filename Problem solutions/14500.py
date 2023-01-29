import sys


DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]


def bfs(start_node, node_list, node_map, loop_num, sum_num, max_num):
    if loop_num == 4:
        max_num[0] = max(max_num[0], sum_num)
        return
    for dx, dy in zip(DX, DY):
        temp_x, temp_y = start_node
        if temp_x + dx == -1 or temp_y + dy == -1:
            continue
        if temp_x + dx == len(node_map) or temp_y + dy == len(node_map[0]):
            continue
        if node_map[temp_x + dx][temp_y + dy]:
            continue
        node_map[temp_x + dx][temp_y + dy] = True
        sum_num += node_list[temp_x + dx][temp_y + dy]
        bfs([temp_x + dx, temp_y + dy], node_list, node_map, loop_num + 1, sum_num, max_num)
        sum_num -= node_list[temp_x + dx][temp_y + dy]
        node_map[temp_x + dx][temp_y + dy] = False


def check_cross(start_node, node_list, max_num):
    temp_x, temp_y = start_node
    temp_list = []
    for dx, dy in zip(DX, DY):
        if temp_x + dx == -1 or temp_y + dy == -1:
            continue
        if temp_x + dx == len(node_list) or temp_y + dy == len(node_list[0]):
            continue
        temp_list.append(node_list[temp_x + dx][temp_y + dy])
    if len(temp_list) < 3:
        return
    if len(temp_list) == 3:
        max_num[0] = max(max_num[0], sum(temp_list) + node_list[temp_x][temp_y])
        return
    max_num[0] = max(max_num[0], sum(temp_list) - min(temp_list) + node_list[temp_x][temp_y])
    return


def main():
    height_num, width_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    node_list = [list(map(int, sys.stdin.readline().rstrip().split(sep=' '))) for _ in range(height_num)]
    node_map = [[False] * width_num for _ in range(height_num)]

    max_num = [0]
    for temp_height in range(height_num):
        for temp_width in range(width_num):
            node_map[temp_height][temp_width] = True
            bfs([temp_height, temp_width], node_list, node_map, 1, node_list[temp_height][temp_width], max_num)
            node_map[temp_height][temp_width] = False
            check_cross([temp_height, temp_width], node_list, max_num)
    print(max_num[0])

    return


if __name__ == "__main__":
    main()
