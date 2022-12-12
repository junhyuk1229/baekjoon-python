import sys


def get_five_num(input_num):
    five_num = 5
    output_num = 0
    while five_num <= input_num:
        output_num += input_num // five_num
        five_num *= 5
    return output_num


def main():
    n, m = map(int, sys.stdin.readline().split(sep=' '))
    print(get_five_num(n) - get_five_num(m) - get_five_num(n - m))


if __name__ == "__main__":
    main()
