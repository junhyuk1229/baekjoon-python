import sys


def main() -> None:
    input_num = int(sys.stdin.readline().rstrip())

    print(f"{input_num * (input_num - 1) // 2}\n2")

    return


if __name__ == '__main__':
    main()
