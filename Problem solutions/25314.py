import sys


def main() -> None:
    input_num = int(sys.stdin.readline().rstrip())

    long_num = input_num // 4

    print('long ' * long_num + 'int')


if __name__ == '__main__':
    main()
