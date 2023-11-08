import sys


def get_gcd(first_num, second_num):
    while second_num > 0:
        temp_num = first_num % second_num
        first_num, second_num = second_num, temp_num

    return first_num


def main() -> None:
    first_num, second_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    if first_num < second_num:
        second_num, first_num = first_num, second_num

    print(first_num * second_num // get_gcd(first_num, second_num))

    return


if __name__ == "__main__":
    main()
