import sys, math


def main():
    length_num = int(sys.stdin.readline().rstrip())
    if length_num % 2 == 1:
        print(0)
        return
    length_num //= 2
    output_list = [3, 2]
    for _ in range(length_num - 1):
        first_num = output_list[0] * 3 + output_list[1]
        second_num = output_list[0] * 2 + output_list[1]
        output_list = [first_num, second_num]
    print(output_list[0])
    return


if __name__ == "__main__":
    main()
