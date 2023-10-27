import sys


def main() -> None:
    level_num = int(sys.stdin.readline().rstrip())

    for t in range(-level_num + 1, level_num):
        print(' ' * abs(t) + '*' * (2 * (level_num - abs(t)) - 1))


if __name__ == '__main__':
    main()
