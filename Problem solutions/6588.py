import sys


MAX_NUM = 1000000


def make_list(list_size: int) -> list:
    output_list = [True] * (list_size + 1)
    for temp_index in range(3, list_size + 1, 2):
        if not output_list[temp_index]:
            continue
        temp_num = temp_index
        while temp_num + temp_index <= list_size:
            temp_num += temp_index
            output_list[temp_num] = False

    return output_list


def main() -> None:
    check_list = make_list(MAX_NUM)
    input_int = int(sys.stdin.readline().rstrip())
    while input_int != 0:
        for temp_val in range(3, input_int // 2 + 1, 2):
            if check_list[temp_val] and check_list[input_int - temp_val]:
                print("{0} = {1} + {2}".format(input_int, temp_val, input_int - temp_val))
                break
            temp_val += 2
        input_int = int(sys.stdin.readline().rstrip())


if __name__ == "__main__":
    main()
