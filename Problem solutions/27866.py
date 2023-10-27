import sys


def main() -> None:
    input_str = sys.stdin.readline().rstrip()
    index_num = int(sys.stdin.readline().rstrip())

    print(input_str[index_num - 1])


if __name__ == '__main__':
    main()
