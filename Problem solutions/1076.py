import sys


CONV_DICT = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}


def main() -> None:
    output_num = CONV_DICT[sys.stdin.readline().rstrip()]
    output_num = 10 * output_num + CONV_DICT[sys.stdin.readline().rstrip()]
    output_num *= 10 ** CONV_DICT[sys.stdin.readline().rstrip()]

    print(output_num)

    return


if __name__ == '__main__':
    main()
