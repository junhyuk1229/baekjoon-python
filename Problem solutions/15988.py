import sys


def main():
    case_num = int(sys.stdin.readline().rstrip())
    check_arr = [0, 1, 2, 4]
    for _ in range(case_num):
        check_num = int(sys.stdin.readline().rstrip())
        while check_num + 1 > len(check_arr):
            check_arr.append((check_arr[-1] + check_arr[-2] + check_arr[-3]) % 1000000009)
        print(check_arr[check_num])
    return


if __name__ == "__main__":
    main()
