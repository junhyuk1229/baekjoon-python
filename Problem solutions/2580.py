import sys


def check_pos(sudoku_arr, x, y):
    same_flag = True
    for index in range(9):
        if sudoku_arr[x][index] == sudoku_arr[x][y] and index != y:
            return True
        if sudoku_arr[index][y] == sudoku_arr[x][y] and index != x:
            return True
        if sudoku_arr[x // 3 * 3 + index // 3][y // 3 * 3 + index % 3] == sudoku_arr[x][y]:
            if same_flag:
                same_flag = False
            else:
                return True
    return False


def sudoku_solve(sudoku_arr, zero_arr, temp_pos):
    if len(zero_arr) == temp_pos:
        return True
    zero_pos = zero_arr[temp_pos]
    for temp_num in range(1, 10):
        sudoku_arr[zero_pos[0]][zero_pos[1]] = temp_num
        if check_pos(sudoku_arr, zero_pos[0], zero_pos[1]):
            sudoku_arr[zero_pos[0]][zero_pos[1]] = 0
            continue
        if sudoku_solve(sudoku_arr, zero_arr, temp_pos + 1):
            return True
        sudoku_arr[zero_pos[0]][zero_pos[1]] = 0


def main():
    sudoku_arr = []
    zero_arr = []
    for i in range(9):
        input_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
        sudoku_arr.append(input_arr)
        for j in range(9):
            if sudoku_arr[i][j] == 0:
                zero_arr.append([i, j])
    sudoku_solve(sudoku_arr, zero_arr, 0)
    for i in range(9):
        print(' '.join(map(str, sudoku_arr[i])))


if __name__ == "__main__":
    main()
