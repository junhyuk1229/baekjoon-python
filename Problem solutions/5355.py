import sys


def main():
    case_num = int(sys.stdin.readline().rstrip())
    for _ in range(case_num):
        input_arr = sys.stdin.readline().rstrip().split(sep=' ')
        output_num = float(input_arr[0])
        for temp_char in input_arr[1:]:
            if temp_char == '@':
                output_num *= 3
            elif temp_char == '%':
                output_num += 5
            else:
                output_num -= 7
        print(f"{output_num:.2f}")


if __name__ == "__main__":
    main()