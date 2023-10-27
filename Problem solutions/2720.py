import sys


def main() -> None:
    case_num = int(sys.stdin.readline().rstrip())

    for _ in range(case_num):
        money_num = int(sys.stdin.readline().rstrip())

        quarter_num = money_num // 25
        money_num -= quarter_num * 25

        dime_num = money_num // 10
        money_num -= dime_num * 10

        nickel_num = money_num // 5
        money_num -= nickel_num * 5

        penny_num = money_num
        money_num -= penny_num

        print(f"{quarter_num} {dime_num} {nickel_num} {penny_num}")


if __name__ == '__main__':
    main()
