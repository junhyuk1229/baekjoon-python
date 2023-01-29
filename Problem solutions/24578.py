import sys


def main():
    input_num = int(sys.stdin.readline().rstrip())
    input_list = []
    for _ in range(4):
        input_list.append(input_num % 10)
        input_num //= 10
    input_list = input_list[::-1]

    check_num = 8
    while check_num > 0:
        print_list = []
        for temp_index, temp_num in enumerate(input_list):
            if temp_index == 2:
                print_list.append(' ')
            if temp_num >= check_num:
                print_list.append('*')
                input_list[temp_index] -= check_num
            else:
                print_list.append('.')
        check_num //= 2
        print(' '.join(print_list))
    return


if __name__ == "__main__":
    main()
