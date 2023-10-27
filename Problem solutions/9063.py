import sys


MINNUM = -10001
MAXNUM = 10001


def main() -> None:
    point_num = int(sys.stdin.readline().rstrip())

    min_x = min_y = MAXNUM
    max_x = max_y = MINNUM

    for _ in range(point_num):
        input_x, input_y = map(int, sys.stdin.readline().rstrip().split(sep=' '))
        min_x = min(min_x, input_x)
        max_x = max(max_x, input_x)
        min_y = min(min_y, input_y)
        max_y = max(max_y, input_y)

    print((max_x - min_x) * (max_y - min_y))


if __name__ == '__main__':
    main()
