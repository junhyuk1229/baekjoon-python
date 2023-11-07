import sys


def main() -> None:
    from_hour, from_min = map(int, sys.stdin.readline().rstrip().split(sep=':'))
    to_hour, to_min = map(int, sys.stdin.readline().rstrip().split(sep=':'))

    if to_min < from_min:
        to_min += 60
        to_hour -= 1

    button_num = to_min - from_min

    if to_hour < from_hour:
        to_hour += 24

    button_num += to_hour - from_hour

    print(button_num)

    return


if __name__ == "__main__":
    main()
