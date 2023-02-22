import sys, math


def main() -> None:
    input_len = int(sys.stdin.readline().rstrip())
    check_list = [math.inf] * 9
    first_input = list(map(int, sys.stdin.readline().rstrip().split()))

    for i in range(3):
        check_list[4 * i] = first_input[i]

    for _ in range(input_len - 1):
        temp_input = list(map(int, sys.stdin.readline().rstrip().split()))
        copy_list = check_list.copy()

        for temp_index in range(3):
            for temp_temp_index in range(3):
                min_val = math.inf
                if temp_index != 0:
                    min_val = min(min_val, copy_list[temp_temp_index])
                if temp_index != 1:
                    min_val = min(min_val, copy_list[temp_temp_index + 3])
                if temp_index != 2:
                    min_val = min(min_val, copy_list[temp_temp_index + 6])
                check_list[3 * temp_index + temp_temp_index] = min_val + temp_input[temp_index]

    min_num = math.inf
    for temp_index, temp_val in enumerate(check_list):
        if temp_index % 4 == 0:
            continue
        min_num = min(min_num, temp_val)

    print(min_num)

    return


if __name__ == "__main__":
    main()
