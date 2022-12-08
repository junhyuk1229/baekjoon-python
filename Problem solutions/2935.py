import sys
import math


def main():
    first_zeros = len(sys.stdin.readline().rstrip())
    symbol = sys.stdin.readline().rstrip()
    second_zeros = len(sys.stdin.readline().rstrip())
    if symbol == '*':
        print(1, end='')
        for _ in range(first_zeros + second_zeros - 2):
            print(0, end='')
    else:
        if first_zeros == second_zeros:
            print(int(2 * math.pow(10, first_zeros - 1)))
            return 0
        max_num = max(first_zeros, second_zeros)
        for i in range(max(first_zeros, second_zeros)):
            if max_num - first_zeros == i or max_num - second_zeros == i:
                print(1, end='')
            else:
                print(0, end='')
    print()


if __name__ == "__main__":
    main()