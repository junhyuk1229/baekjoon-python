import sys


# Used to get move direction in coordinates
move_dict = {
    'R': [1, 0],
    'L': [-1, 0],
    'B': [0, -1],
    'T': [0, 1],
    'RT': [1, 1],
    'RB': [1, -1],
    'LT': [-1, 1],
    'LB': [-1, -1],
}


'''
def print_log(success_code, move_dir, king_pos, stone_pos):
    if success_code == 0:
        print("Movement blocked")
    elif success_code == 1:
        print("King moved")
    else:
        print("Stone moved")
    print(f"King position: {king_pos}")
    print(f"Stone position: {stone_pos}")
    print(f"Move dir: {move_dir[0]}, {move_dir[1]}")
    print()
'''


def main() -> None:
    # Get input
    temp_king_pos, temp_stone_pos, input_num = sys.stdin.readline().rstrip().split(sep=' ')

    '''
    print(f"Position of king = {temp_king_pos}")
    print(f"Position of stone = {temp_stone_pos}")
    print(f"Input number = {input_num}")
    print()
    '''

    # Process input
    king_pos = [ord(temp_king_pos[0]) - ord('A') + 1, int(temp_king_pos[1])]
    stone_pos = [ord(temp_stone_pos[0]) - ord('A') + 1, int(temp_stone_pos[1])]

    '''
    print(f"Position of king = {king_pos}")
    print(f"Position of stone = {stone_pos}")
    print()
    '''

    # Loop till all input is checked
    for _ in range(int(input_num)):
        # Get moved position
        temp_dx, temp_dy = move_dict[sys.stdin.readline().rstrip()]
        move_king_pos = [king_pos[0] + temp_dx, king_pos[1] + temp_dy]
        # If moved king position is out of bounds ignore input
        if move_king_pos[0] * move_king_pos[1] == 0:
            # print_log(0, [temp_dx, temp_dy], king_pos, stone_pos)
            continue
        if move_king_pos[0] == 9 or move_king_pos[1] == 9:
            # print_log(0, [temp_dx, temp_dy], king_pos, stone_pos)
            continue
        # If moved king position overlaps with stone position
        if move_king_pos == stone_pos:
            # Get moved position
            move_stone_pos = [stone_pos[0] + temp_dx, stone_pos[1] + temp_dy]
            # If moved stone position is out of bounds ignore input(even the king's movement)
            if move_stone_pos[0] * move_stone_pos[1] == 0:
                # print_log(0, [temp_dx, temp_dy], king_pos, stone_pos)
                continue
            if move_stone_pos[0] == 9 or move_stone_pos[1] == 9:
                # print_log(0, [temp_dx, temp_dy], king_pos, stone_pos)
                continue
            # Update stone position
            stone_pos = move_stone_pos
            # print_log(2, [temp_dx, temp_dy], king_pos, stone_pos)
        # Update king position
        king_pos = move_king_pos
        # print_log(1, [temp_dx, temp_dy], king_pos, stone_pos)

    '''
    # Print output
    print(king_pos)
    print(stone_pos)
    print()
    '''

    # Process output
    output_king_pos = ""
    output_stone_pos = ""
    output_king_pos += chr(ord('A') + king_pos[0] - 1)
    output_king_pos += f"{king_pos[1]}"
    output_stone_pos += chr(ord('A') + stone_pos[0] - 1)
    output_stone_pos += f"{stone_pos[1]}"

    # Print output
    print(output_king_pos + '\n' + output_stone_pos)

    return


if __name__ == '__main__':
    main()
