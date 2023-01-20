import sys, math


def main():
    input_num = int(sys.stdin.readline().rstrip())
    input_arr = [math.inf] * (input_num + 1)
    temp_num = 1
    while temp_num ** 2 <= input_num:
        input_arr[temp_num ** 2] = 1
        for temp_index in range(1, input_num - temp_num ** 2 + 1):
            input_arr[temp_index + temp_num ** 2] = min(input_arr[temp_index] + 1, input_arr[temp_index + temp_num ** 2])
        temp_num += 1
    print(input_arr[-1])
    return


if __name__ == "__main__":
    main()
