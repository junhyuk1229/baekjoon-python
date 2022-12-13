import sys


def fibo_memo(memo_arr, check_num):
    if memo_arr[check_num] == 0:
        memo_arr[check_num] = fibo_memo(memo_arr, check_num - 1) + fibo_memo(memo_arr, check_num - 2)
    return memo_arr[check_num]


def main():
    check_num = int(sys.stdin.readline().rstrip())
    memo_arr = [0 for _ in range(check_num + 1)]
    memo_arr[1] = memo_arr[2] = 1
    print(f"{fibo_memo(memo_arr, check_num)} {check_num - 2}")


if __name__ == "__main__":
    main()
