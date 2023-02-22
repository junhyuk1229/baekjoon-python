import sys


def find_max_height(input_map: list, check_row: int) -> int:
    output_num = 0
    comp_char = ''
    temp_num = 0
    for temp_char in input_map[check_row]:
        if temp_char != comp_char:
            output_num = max(output_num, temp_num)
            comp_char = temp_char
            temp_num = 1
        else:
            temp_num += 1
    output_num = max(output_num, temp_num)
    return output_num


def find_max_width(input_map: list, check_col: int) -> int:
    output_num = 0
    comp_char = ''
    temp_num = 0
    for temp_index in range(len(input_map)):
        if input_map[temp_index][check_col] != comp_char:
            output_num = max(output_num, temp_num)
            comp_char = input_map[temp_index][check_col]
            temp_num = 1
        else:
            temp_num += 1
    output_num = max(output_num, temp_num)
    return output_num


def main() -> None:
    input_size = int(sys.stdin.readline().rstrip())
    input_map = []
    for _ in range(input_size):
        input_map.append(list(sys.stdin.readline().rstrip()))

    output_num = 0
    for temp_num in range(input_size):
        output_num = max(output_num, find_max_height(input_map, temp_num))
        output_num = max(output_num, find_max_width(input_map, temp_num))

    for temp_height in range(input_size):
        for temp_width in range(input_size - 1):
            input_map[temp_height][temp_width], input_map[temp_height][temp_width + 1] = input_map[temp_height][temp_width + 1], input_map[temp_height][temp_width]
            output_num = max(output_num, find_max_height(input_map, temp_height))
            output_num = max(output_num, find_max_width(input_map, temp_width))
            output_num = max(output_num, find_max_width(input_map, temp_width + 1))
            input_map[temp_height][temp_width], input_map[temp_height][temp_width + 1] = input_map[temp_height][temp_width + 1], input_map[temp_height][temp_width]

    for temp_height in range(input_size - 1):
        for temp_width in range(input_size):
            input_map[temp_height][temp_width], input_map[temp_height + 1][temp_width] = input_map[temp_height + 1][temp_width], input_map[temp_height][temp_width]
            output_num = max(output_num, find_max_height(input_map, temp_height))
            output_num = max(output_num, find_max_height(input_map, temp_height + 1))
            output_num = max(output_num, find_max_width(input_map, temp_width))
            input_map[temp_height][temp_width], input_map[temp_height + 1][temp_width] = input_map[temp_height + 1][temp_width], input_map[temp_height][temp_width]

    print(output_num)

    return


if __name__ == "__main__":
  main()
