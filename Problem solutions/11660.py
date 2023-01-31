import sys, math


def update_list(input_list, first_end, second_end, input_len):
    return


def main():
    list_size, output_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    check_list = []
    for temp_height in range(list_size):
        check_list.append(list(map(int, sys.stdin.readline().rstrip().split(sep=' '))))

    for temp_height in range(list_size):
        for temp_width in range(list_size):
            if temp_height != 0:
                check_list[temp_height][temp_width] += check_list[temp_height - 1][temp_width]
            if temp_width != 0:
                check_list[temp_height][temp_width] += check_list[temp_height][temp_width - 1]
            if temp_height * temp_width != 0:
                check_list[temp_height][temp_width] -= check_list[temp_height - 1][temp_width - 1]

    for _ in range(output_num):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split(sep=' '))
        temp_num = check_list[x2 - 1][y2 - 1]
        if y1 - 2 >= 0:
            temp_num -= check_list[x2 - 1][y1 - 2]
        if x1 - 2 >= 0:
            temp_num -= check_list[x1 - 2][y2 - 1]
        if x1 - 2 >= 0 and y1 - 2 >= 0:
            temp_num += check_list[x1 - 2][y1 - 2]
        print(temp_num)
    return


if __name__ == "__main__":
    main()
