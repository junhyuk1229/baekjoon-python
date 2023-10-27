import sys


def main() -> None:
    input_num = int(sys.stdin.readline().rstrip())

    print((pow(2, input_num) + 1) ** 2)


if __name__ == '__main__':
    main()
