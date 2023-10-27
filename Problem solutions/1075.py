import sys


def main() -> None:
    input_str = int(sys.stdin.readline().rstrip())

    div_num = int(sys.stdin.readline().rstrip())

    temp_num = div_num - 100 * (input_str // 100) % div_num

    if temp_num == div_num:
        temp_num = 0

    temp_num = str(temp_num)

    if len(temp_num) == 1:
        temp_num = '0' + temp_num

    print(temp_num)

    return


if __name__ == '__main__':
    main()
