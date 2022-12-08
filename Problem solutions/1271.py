import sys


def main():
    money_num, people_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    print(money_num // people_num)
    print(money_num % people_num)


if __name__ == "__main__":
    main()
