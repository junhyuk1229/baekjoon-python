import math
import sys


def main() -> None:
    input_num, index_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    numerator_list = []
    numerator_num = 1
    i = 1

    while i <= input_num:
        if input_num % i == 0:
            numerator_list.append(i)
            numerator_num += 1

        i += 1

    if len(numerator_list) < index_num:
        print(0)
        return

    print(numerator_list[index_num - 1])


if __name__ == '__main__':
    main()
