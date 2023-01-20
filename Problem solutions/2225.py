import sys


def main():
    list_len, round_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    output_arr = [1] * (list_len + 1)
    while round_num > 1:
        for temp_index in range(1, list_len + 1):
            output_arr[temp_index] += output_arr[temp_index - 1]
            output_arr[temp_index] %= 1000000000
        round_num -= 1
    print(output_arr[-1])


if __name__ == "__main__":
    main()
