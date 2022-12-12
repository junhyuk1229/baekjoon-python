import sys


def main():
    row_num = col_num = max_num = 0
    for i in range(9):
        temp_input = list(map(int, sys.stdin.readline().split(sep=' ')))
        for j in range(9):
            if temp_input[j] > max_num:
                max_num = temp_input[j]
                row_num = i
                col_num = j
    print("%d\n%d %d" % (max_num, row_num + 1, col_num + 1))


if __name__ == "__main__":
    main()
