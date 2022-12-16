import sys


def main():
    input_num = int(sys.stdin.readline().rstrip())
    check_arr = [0 for _ in range(input_num + 1)]
    for temp_index in range(2, input_num + 1):
        min_num = check_arr[temp_index - 1]
        if temp_index % 2 == 0:
            min_num = min(min_num, check_arr[temp_index // 2])
        if temp_index % 3 == 0:
            min_num = min(min_num, check_arr[temp_index // 3])
        check_arr[temp_index] = min_num + 1
    print(check_arr[input_num])


if __name__ == "__main__":
    main()
