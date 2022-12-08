import sys


def main():
    case_num = int(sys.stdin.readline().rstrip())
    for _ in range(case_num):
        first_num, second_num = map(int, sys.stdin.readline().split(sep=' '))
        check_div = min(first_num, second_num)
        while check_div > 1:
            if first_num % check_div == 0 and second_num % check_div == 0:
                break
            check_div -= 1
        print(first_num * second_num // check_div)


if __name__ == "__main__":
    main()
