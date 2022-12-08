import sys


def main():
    first_num, avg_num = map(int, sys.stdin.readline().split(sep=' '))
    print(2*avg_num - first_num)


if __name__ == "__main__":
    main()