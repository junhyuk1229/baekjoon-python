import sys


def main() -> None:
    input_height, input_width = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    input_list = [list(map(int, sys.stdin.readline().rstrip().split(sep=' '))) for _ in range(input_height)]
    case_num = int(sys.stdin.readline().rstrip())

    for _ in range(case_num):
        first_x, first_y, second_x, second_y = map(int, sys.stdin.readline().rstrip().split(sep=' '))
        first_x -= 1
        first_y -= 1
        second_x -= 1
        second_y -= 1

        output_num = 0

        for temp_line_index in range(first_x, second_x + 1):
            output_num += sum(input_list[temp_line_index][first_y:second_y + 1])

        print(output_num)


if __name__ == "__main__":
    main()
