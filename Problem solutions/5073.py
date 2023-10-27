import sys


def main() -> None:
    input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))

    while input_list != [0] * 3:
        max_num = max(input_list)
        min_num = min(input_list)
        list_sum = sum(input_list)
        mid_num = list_sum - max_num - min_num

        if 2 * max_num >= list_sum:
            print("Invalid")
        elif max_num == min_num == mid_num:
            print("Equilateral")
        elif max_num == min_num or min_num == mid_num or mid_num == max_num:
            print("Isosceles")
        else:
            print("Scalene")

        input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))

    return


if __name__ == '__main__':
    main()
