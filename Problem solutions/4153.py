import sys


def main():
    line_len = list(map(int, sys.stdin.readline().split(sep=' ')))
    total_num = 0
    while line_len != [0, 0, 0] :
        for temp_num in line_len:
            total_num += temp_num * temp_num
        max_num = max(line_len)
        total_num -= max_num * max_num * 2
        if total_num == 0:
            print("right")
        else:
            print("wrong")
        total_num = 0
        line_len = list(map(int, sys.stdin.readline().split(sep=' ')))


if __name__ == "__main__":
    main()
