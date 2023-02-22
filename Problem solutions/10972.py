import sys


def main() -> None:
    input_num = int(sys.stdin.readline().rstrip())
    check_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))

    change_index = input_num - 1
    while change_index != 0 and check_list[change_index - 1] > check_list[change_index]:
        change_index -= 1

    if change_index == 0:
        print(-1)
        return

    change_index -= 1

    target_index = 0
    target_min = input_num
    for temp_index, temp_val in enumerate(check_list[change_index + 1:]):
        if target_min > temp_val > check_list[change_index]:
            target_min = temp_val
            target_index = temp_index

    target_index += change_index + 1

    check_list[change_index], check_list[target_index] = check_list[target_index], check_list[change_index]
    temp_list = check_list[change_index + 1:]
    temp_list.sort()

    print(' '.join(map(str, check_list[:change_index + 1] + temp_list)))

    return


if __name__ == "__main__":
    main()
