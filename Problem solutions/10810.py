import sys


def main() -> None:
    input_len, case_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    basket_list = [0] * (input_len + 1)

    for _ in range(case_num):
        start_index, end_index, ball_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))

        for temp_index in range(start_index, end_index + 1):
            basket_list[temp_index] = ball_num

    print(' '.join(map(str, basket_list[1:])))


if __name__ == '__main__':
    main()
