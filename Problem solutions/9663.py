import sys

'''
def queen_repeat(queen_arr, board_size, input_pos):
    if input_pos == board_size:
        queen_arr[board_size] += 1
        return
    for temp_queen_num in range(board_size):
        invalid_pos_flag = 0
        for temp_comp_pos in range(input_pos):
            if queen_arr[temp_comp_pos] == temp_queen_num:
                invalid_pos_flag = 1
                break
            if abs(temp_comp_pos - input_pos) == abs(queen_arr[temp_comp_pos] - temp_queen_num):
                invalid_pos_flag = 1
                break
        if invalid_pos_flag:
            continue
        queen_arr[input_pos] = temp_queen_num
        queen_repeat(queen_arr, board_size, input_pos + 1)


def main():
    board_size = int(sys.stdin.readline().rstrip())
    input_arr = [-1] * (board_size + 1)
    input_arr[board_size] = 0
    queen_repeat(input_arr, board_size, 0)
    print(input_arr[board_size])
'''


def queen_repeat(check_arr, board_size, input_pos):
    if input_pos == board_size:
        check_arr[0][board_size] += 1
        return
    for temp_queen_num in range(board_size):
        if check_arr[0][temp_queen_num] == 1:
            continue
        if check_arr[1][temp_queen_num + input_pos] == 1:
            continue
        if check_arr[2][temp_queen_num - input_pos + board_size - 1] == 1:
            continue
        check_arr[0][temp_queen_num] = 1
        check_arr[1][temp_queen_num + input_pos] = 1
        check_arr[2][temp_queen_num - input_pos + board_size - 1] = 1
        queen_repeat(check_arr, board_size, input_pos + 1)
        check_arr[0][temp_queen_num] = 0
        check_arr[1][temp_queen_num + input_pos] = 0
        check_arr[2][temp_queen_num - input_pos + board_size - 1] = 0
    return


def main():
    board_size = int(sys.stdin.readline().rstrip())
    check_arr = [[0 for _ in range(2 * board_size)] for _ in range(3)]
    queen_repeat(check_arr, board_size, 0)
    print(check_arr[0][board_size])


if __name__ == "__main__":
    main()
