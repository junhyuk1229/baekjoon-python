import sys


def main():
    first_num, second_num = map(int, sys.stdin.readline().split(sep=' '))
    print(abs(first_num - second_num))


if __name__ == "__main__":
    main()
