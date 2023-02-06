import sys
from collections import deque, defaultdict


DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]


def change_int(input_height, pos_list):
    return pos_list[0] * input_height + pos_list[1]


def bfs_coin_move(input_height, input_width, input_list, bfs_queue, pos_dict):
    output_list = deque()
    while bfs_queue:
        first_coin_pos, second_coin_pos = bfs_queue.pop()
        for dx, dy in zip(DX, DY):
            first_h = first_coin_pos[0]
            first_w = first_coin_pos[1]
            second_h = second_coin_pos[0]
            second_w = second_coin_pos[1]
            fall_num = 2
            change_flag = False

            if 0 <= first_h + dx < len(input_list) and 0 <= first_w + dy < len(input_list[0]):
                fall_num -= 1
                if input_list[first_h + dx][first_w + dy] != '#':
                    first_h += dx
                    first_w += dy
                    change_flag = True
            if 0 <= second_h + dx < len(input_list) and 0 <= second_w + dy < len(input_list[0]):
                fall_num -= 1
                if input_list[second_h + dx][second_w + dy] != '#':
                    second_h += dx
                    second_w += dy
                    change_flag = True
            if fall_num == 1:
                return deque()
            elif fall_num == 2 or not change_flag:
                continue

            if first_h == second_h and first_w == second_w:
                continue
            pos_dict[change_int(input_height, [first_h, first_w])][change_int(input_height, [first_h, first_w])] = True
            output_list.append([[first_h, first_w], [second_h, second_w]])
    return output_list


def loop_coin_move(input_height, input_width, input_list, coin_pos):
    output_num = 0
    bfs_queue = deque([coin_pos])
    pos_dict = defaultdict(lambda: defaultdict(bool))
    pos_dict[change_int(input_height, coin_pos[0])][change_int(input_height, coin_pos[1])] = True
    while output_num <= 10:
        bfs_queue = bfs_coin_move(input_height, input_width, input_list, bfs_queue, pos_dict)
        if not bfs_queue:
            return -1
        output_num += 1
    if output_num > 10:
        return -1
    return output_num


def main():
    input_height, input_width = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    input_list = []
    coin_pos = []
    for temp_height in range(input_height):
        input_list.append(sys.stdin.readline().rstrip())
        for temp_width in range(input_width):
            if input_list[temp_height][temp_width] != 'o':
                continue
            coin_pos.append([temp_height, temp_width])
    print(coin_pos)
    for temp_list in input_list:
        print(temp_list)

    output_num = loop_coin_move(input_height, input_width, input_list, coin_pos)
    print(output_num)

    return


if __name__ == "__main__":
    main()
