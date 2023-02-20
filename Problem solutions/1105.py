import sys


def main() -> None:
    first_num, second_num = sys.stdin.readline().rstrip().split(sep=' ')
    if len(first_num) != len(second_num):
        print(0)
        return
    output_num = 0
    for temp_first, temp_second in zip(first_num, second_num):
        if temp_first == temp_second:
            if temp_first == '8':
                output_num += 1
        else:
            break
    print(output_num)
    return


if __name__ == '__main__':
    main()
