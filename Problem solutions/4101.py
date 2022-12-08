import sys


def main():
    first_num, second_num = map(int, sys.stdin.readline().split(sep=' '))
    while first_num or second_num:
        if first_num <= second_num:
            print("No")
        else:
            print("Yes")
        first_num, second_num = map(int, sys.stdin.readline().split(sep=' '))


if __name__ == "__main__":
    main()
