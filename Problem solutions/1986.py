import sys


# Constants containing all movement possibilities
KNIGHT_MOVE_X = [-2, -2, -1, -1, 1, 1, 2, 2]
KNIGHT_MOVE_Y = [1, -1, -2, 2, 2, -2, 1, -1]
QUEEN_MOVE_X = [1, 1, 1, -1, -1, -1, 0, 0]
QUEEN_MOVE_Y = [0, -1, 1, -1, 1, 0, -1, 1]


# Get the number of pieces and positions from input
def get_piece_num_pos(piece_list: list):
    piece_num = piece_list[0]
    piece_pos = list()

    for i in range(1, len(piece_list), 2):
        piece_pos.append([piece_list[i] - 1, piece_list[i + 1] - 1])

    return piece_num, piece_pos


# Checks if location is out of range
def out_of_range(input_x, input_y, check_x, check_y):
    if input_x < 0 or input_x >= check_x:
        return True
    if input_y < 0 or input_y >= check_y:
        return True
    return False


def main() -> None:
    board_x, board_y = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    queen_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    knight_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    pawn_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))

    queen_num, queen_pos = get_piece_num_pos(queen_list)
    knight_num, knight_pos = get_piece_num_pos(knight_list)
    pawn_num, pawn_pos = get_piece_num_pos(pawn_list)

    # 0 = Empty, 1 = passed num, 2 = obj
    board_map = [[0] * board_y for _ in range(board_x)]
    board_num = board_x * board_y

    # Check all pawn positions
    for pawn_x, pawn_y in pawn_pos:
        board_map[pawn_x][pawn_y] = 2
    board_num -= pawn_num

    # Check all knight positions
    for knight_x, knight_y in knight_pos:
        # Check all knight movements
        for dx, dy in zip(KNIGHT_MOVE_X, KNIGHT_MOVE_Y):
            if out_of_range(knight_x + dx, knight_y + dy, board_x, board_y):
                continue
            if board_map[knight_x + dx][knight_y + dy] == 0:
                board_map[knight_x + dx][knight_y + dy] = 1
                board_num -= 1
        # Set knight position
        if board_map[knight_x][knight_y] == 0:
            board_num -= 1
        board_map[knight_x][knight_y] = 2

    # Check all queen positions
    for queen_x, queen_y in queen_pos:
        # Check all queen movements
        for inc_x, inc_y in zip(QUEEN_MOVE_X, QUEEN_MOVE_Y):
            dx, dy = inc_x, inc_y
            # While the tile is not out of range and the position is not blocked
            while not out_of_range(queen_x + dx, queen_y + dy, board_x, board_y) and board_map[queen_x + dx][queen_y + dy] < 2:
                # Mark the tile
                if board_map[queen_x + dx][queen_y + dy] == 0:
                    board_map[queen_x + dx][queen_y + dy] = 1
                    board_num -= 1
                # Move one tile
                dy += inc_y
                dx += inc_x
        # Set queen position
        if board_map[queen_x][queen_y] == 0:
            board_num -= 1
        board_map[queen_x][queen_y] = 2

    print(board_num)


if __name__ == '__main__':
    main()
