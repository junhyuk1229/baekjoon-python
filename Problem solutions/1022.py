import sys


def main() -> None:
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    output_list = []
    max_num = 1

    for i, x in enumerate(range(x1, x2 + 1)):
        output_list.append(list())

        for y in range(y1, y2 + 1):
            max_coor = max(abs(x), abs(y))
            temp_num = (2 * max_coor + 1) ** 2

            if x == max_coor:
                temp_num -= max_coor - y
            elif x == -max_coor:
                temp_num -= max_coor * 5 + y
            elif y == max_coor:
                temp_num -= max_coor * 7 + x
            elif y == -max_coor:
                temp_num -= max_coor * 3 - x

            max_num = max(max_num, temp_num)

            output_list[i].append(temp_num)

    digit_num = 1

    while max_num >= 10 ** digit_num:
        digit_num += 1

    for i in output_list:
        for j in i:
            print(f"{j:{digit_num}.0f}", end=' ')
        print('')

    return


if __name__ == '__main__':
    main()
