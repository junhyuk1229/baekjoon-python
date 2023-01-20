import sys
from collections import deque


DX = [-1, 1, 0, 0]
DY = [0, 0, -1, 1]


def move_arr(strip_arr: list, arr_len: int):
    zero_index = 0
    for temp_index in range(arr_len):
        if strip_arr[temp_index] == 0:
            continue
        strip_arr[zero_index], strip_arr[temp_index] = strip_arr[temp_index], strip_arr[zero_index]
        zero_index += 1
    for temp_index in range(arr_len - 1):
        if strip_arr[temp_index] == strip_arr[temp_index + 1]:
            strip_arr[temp_index] *= 2
            for move_index in range(temp_index + 1, arr_len - 1):
                strip_arr[move_index] = strip_arr[move_index + 1]
            strip_arr[arr_len - 1] = 0


def bfs_board(board_map: deque, arr_len: int) -> deque:
    output_queue = deque()
    while board_map:
        temp_board = board_map.pop()
        # up press
        moved_board = temp_board.copy()
        for temp_width in range(arr_len):
            temp_strip = []
            for temp_height in range(arr_len):
                temp_strip.append(moved_board[temp_height][temp_width])
            move_arr(temp_strip, arr_len)
            for temp_height in range(arr_len):
                moved_board[temp_height][temp_width] = temp_strip[temp_height]
        output_queue.append(moved_board)
        # down press
        moved_board = temp_board.copy()
        for temp_width in range(arr_len):
            temp_strip = []
            for temp_height in range(arr_len):
                temp_strip.append(moved_board[arr_len - temp_height - 1][temp_width])
            move_arr(temp_strip, arr_len)
            for temp_height in range(arr_len):
                moved_board[arr_len - temp_height - 1][temp_width] = temp_strip[temp_height]
        output_queue.append(moved_board)
        # left press
        moved_board = temp_board.copy()
        for temp_height in range(arr_len):
            move_arr(moved_board[temp_height], arr_len)
        output_queue.append(moved_board)
        # right press
        moved_board = temp_board.copy()
        for temp_height in range(arr_len):
            temp_strip = moved_board[temp_height][::-1]
            move_arr(temp_strip, arr_len)
            for temp_width in range(arr_len):
                moved_board[temp_height][temp_width] = temp_strip[arr_len - temp_width - 1]
        output_queue.append(moved_board)
    return output_queue


def search_max_block(start_board: list, depth_num: int):
    temp_queue = deque([start_board])
    for _ in range(depth_num):
        temp_queue = bfs_board(temp_queue)



def main() -> None:
    # Get input
    board_size = int(sys.stdin.readline().rstrip())
    board_map = []
    for _ in range(board_size):
        board_map.append(list(map(int, sys.stdin.readline().rstrip().split(sep=' '))))


if __name__ == "__main__":
    # main()
    a = [2, 2, 4, 4]
    b = [[2, 2, 2], [4, 4, 4], [8, 8, 8]]
    move_arr(a, 3)
    print(a)
    bfs_board(deque([b]), 3)
