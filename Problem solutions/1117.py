import sys


def main() -> None:
    W, H, f, c, x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    double_w = f
    if f > W / 2:
        double_w = W - f

    paint_num = 0
    x3 = min(x2, double_w)
    double_paint_num = ((x3 - x1) * (y2 - y1)) * (c + 1) * 2
    if double_paint_num > 0:
        paint_num += double_paint_num
    x3 = max(x1, double_w)
    one_paint_num = ((x2 - x3) * (y2 - y1)) * (c + 1)
    if one_paint_num > 0:
        paint_num += one_paint_num

    print(W * H - paint_num)

    return


if __name__ == '__main__':
    main()
