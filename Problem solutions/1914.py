import sys


def move_level(level: int, move_from: int, move_to: int) -> None:
    if level == 1:
        print(move_from, move_to)
        return

    other_loc = 6 - move_from - move_to
    move_level(level - 1, move_from, other_loc)
    print(move_from, move_to)
    move_level(level - 1, other_loc, move_to)

    return


def main() -> None:
    input_num = int(sys.stdin.readline().rstrip())

    print(pow(2, input_num) - 1)

    if input_num <= 20:
        move_level(input_num, 1, 3)


if __name__ == '__main__':
    main()
