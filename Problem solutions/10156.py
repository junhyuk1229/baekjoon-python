import sys


def main():
    cookie_cost, cookie_num, cur_money = map(int, sys.stdin.readline().split(sep=' '))
    if cookie_cost * cookie_num >= cur_money:
        print(cookie_cost * cookie_num - cur_money)
    else:
        print(0)


if __name__ == "__main__":
    main()
