import sys


def custom_func(a, b, c, input_arr):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return custom_func(20, 20, 20, input_arr)
    if input_arr[a][b][c] != 0:
        return input_arr[a][b][c]
    if a < b < c:
        input_arr[a][b][c] = custom_func(a, b, c - 1, input_arr) + custom_func(a, b - 1, c - 1, input_arr) - custom_func(a, b - 1, c, input_arr)
    else:
        input_arr[a][b][c] = custom_func(a - 1, b, c, input_arr) + custom_func(a - 1, b - 1, c, input_arr) + custom_func(a - 1, b, c - 1, input_arr) - custom_func(a - 1, b - 1, c - 1, input_arr)
    return input_arr[a][b][c]


def main():
    input_arr = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
    a, b, c = map(int, sys.stdin.readline().split(sep=' '))
    while a != -1 or b != -1 or c != -1:
        print(f"w({a}, {b}, {c}) = {custom_func(a, b, c, input_arr)}")
        a, b, c = map(int, sys.stdin.readline().split(sep=' '))


if __name__ == "__main__":
    main()
