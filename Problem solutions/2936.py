import sys


def get_ans(input_coor):
    if input_coor[0] == 0:
        if input_coor[1] <= 125:
            temp_height = 250.0 ** 2.0 / 2.0 / (250 - input_coor[1])
            return [temp_height, 250 - temp_height]
        temp_height = 250.0 ** 2.0 / 2.0 / input_coor[1]
        return [temp_height, 0]
    elif input_coor[1] == 0:
        input_coor[1], input_coor[0] = input_coor[0], input_coor[1]
        temp_coor = get_ans(input_coor)
        return [temp_coor[1], temp_coor[0]]
    else:
        temp_height = input_coor[1]
        if input_coor[0] >= 125:
            temp_height = input_coor[0]
        temp_width = 250 - 250.0 ** 2.0 / 2.0 / temp_height
        if input_coor[0] >= 125:
            return [0, temp_width]
        return [temp_width, 0]


def main():
    input_coor = list(map(float, sys.stdin.readline().rstrip().split(sep=' ')))
    output_coor = get_ans(input_coor)
    output_coor[0] = round(output_coor[0], 2)
    output_coor[1] = round(output_coor[1], 2)
    print("{:.2f} {:.2f}".format(output_coor[0], output_coor[1]))
    return


if __name__ == '__main__':
    main()
