import sys


def GCD(first_num, second_num):
    while second_num != 0:
        rem_num = first_num % second_num
        first_num = second_num
        second_num = rem_num
    return first_num


def main():
    input_num = int(sys.stdin.readline().rstrip())
    input_arr = list(map(int, sys.stdin.readline().split(sep=' ')))
    output_num = input_arr[0]
    for index_num in range(input_num - 1):
        GCD_num = GCD(output_num, input_arr[index_num + 1])
        print(f"{output_num // GCD_num}/{input_arr[index_num + 1] // GCD_num}")


if __name__ == "__main__":
    main()
