import sys


def triangle_output(memo_arr, input_num):
    if len(memo_arr) - 1 < input_num:
        for _ in range(input_num - len(memo_arr) + 1):
            memo_arr.append(0)
    if memo_arr[input_num] == 0:
        memo_arr[input_num] = triangle_output(memo_arr, input_num - 1) + triangle_output(memo_arr, input_num - 5)
    return memo_arr[input_num]


def main():
    case_num = int(sys.stdin.readline().rstrip())
    memo_arr = [0, 1, 1, 1, 2, 2]
    for _ in range(case_num):
        input_num = int(sys.stdin.readline().rstrip())
        print(triangle_output(memo_arr, input_num))


if __name__ == "__main__":
    main()
