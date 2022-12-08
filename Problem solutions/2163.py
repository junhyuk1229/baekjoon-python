import sys


def main():
    height_num, width_num = map(int, sys.stdin.readline().split(sep=' '))
    print(height_num*width_num - 1)


if __name__ == "__main__":
    main()