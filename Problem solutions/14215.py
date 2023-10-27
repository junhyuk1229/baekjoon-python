import sys


def main() -> None:
    temp_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))

    total_sum = sum(temp_list)
    max_num = max(temp_list)

    if 2 * max_num >= total_sum:
        print(2 * (total_sum - max_num) - 1)
    else:
        print(total_sum)

    return


if __name__ == '__main__':
    main()
