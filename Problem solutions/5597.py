import sys


def main():
    check_arr = [1] * 30
    for _ in range(28):
        temp_int = int(sys.stdin.readline().rstrip())
        check_arr[temp_int - 1] = 0
    for i in range(30):
        if check_arr[i] == 1:
            print("%d" % (i + 1))


if __name__ == "__main__":
    main()
