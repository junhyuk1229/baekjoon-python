import sys


def main():
    digit_num = int(sys.stdin.readline().rstrip())
    output_arr = [1] * 10
    for _ in range(digit_num - 1):
        for temp_index in range(9):
            output_arr[temp_index + 1] += output_arr[temp_index]
            output_arr[temp_index] %= 10007
    print(sum(output_arr) % 10007)
    return


if __name__ == "__main__":
    main()
