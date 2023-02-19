import sys


def main():
    first_str = sys.stdin.readline().rstrip()
    second_str = sys.stdin.readline().rstrip()
    check_list = [0] * len(first_str)
    for temp_char in second_str:
        temp_list = [0] * len(first_str)
        for temp_index, temp_temp_char in enumerate(first_str):
            if temp_char != temp_temp_char:
                continue
            if temp_index > 0:
                temp_list[temp_index] = max(check_list[:temp_index])
            else:
                temp_list[temp_index] = 0
            temp_list[temp_index] += 1
        print(check_list)
    print(max(check_list))
    return


if __name__ == '__main__':
    main()
