import sys


def main():
    first_num, second_num = map(int, sys.stdin.readline().split(sep=' '))
    while not(first_num == 0 and second_num == 0):
        if first_num % second_num == 0:
            print("multiple")
        elif second_num % first_num == 0:
            print("factor")
        else:
            print("neither")
        first_num, second_num = map(int, sys.stdin.readline().split(sep=' '))


if __name__ == "__main__":
    main()
