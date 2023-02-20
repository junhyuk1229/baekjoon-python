import sys


def flip_list(input_list: list, flip_height: int, flip_width: int) -> None:
    for temp_height in range(flip_height, flip_height + 3):
        for temp_width in range(flip_width, flip_width + 3):
            if input_list[temp_height][temp_width]:
                input_list[temp_height][temp_width] = False
            else:
                input_list[temp_height][temp_width] = True
    return


def main() -> None:
    input_height, input_width = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    first_list = []
    for _ in range(input_height):
        first_list.append(sys.stdin.readline().rstrip())
    output_list = []
    for temp_height in range(input_height):
        output_list.append([])
        temp_list = sys.stdin.readline().rstrip()
        for temp_width in range(input_width):
            if temp_list[temp_width] == first_list[temp_height][temp_width]:
                output_list[temp_height].append(False)
                continue
            output_list[temp_height].append(True)

    output_num = 0
    temp_height = 0
    while temp_height < len(output_list) - 2:
        temp_line = output_list[temp_height]
        temp_width = 0
        while temp_width < len(temp_line) - 2:
            temp_bool = temp_line[temp_width]
            if temp_bool:
                flip_list(output_list, temp_height, temp_width)
                output_num += 1
            temp_width += 1
        if temp_line[-1] or temp_line[-2]:
            output_num = -1
            break
        temp_height += 1

    if output_num != -1:
        for temp_bool in output_list[-1]:
            if temp_bool:
                output_num = -1
                break
    if len(output_list) != 1 and output_num != -1:
        for temp_bool in output_list[-2]:
            if temp_bool:
                output_num = -1
                break

    print(output_num)

    return


if __name__ == '__main__':
    main()
