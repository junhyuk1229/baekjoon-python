import sys


def main():
    first_num, second_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    print((first_num + second_num) * (first_num - second_num))
    return


if __name__ == '__main__':
    main()
