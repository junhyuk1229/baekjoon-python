import sys


def main() -> None:
    height_num = int(sys.stdin.readline().rstrip())

    for temp_num in range(height_num):
        print(' ' * (height_num - temp_num - 1) + '*' * (2 * temp_num + 1))

    return


if __name__ == "__main__":
    main()
