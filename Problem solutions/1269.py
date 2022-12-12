import sys


def main():
    first_len, second_len = map(int, sys.stdin.readline().split(sep=' '))
    first_arr = set(map(int, sys.stdin.readline().split(sep=' ')))
    second_arr = set(map(int, sys.stdin.readline().split(sep=' ')))
    both_num = 0
    for temp_num in second_arr:
        if temp_num in first_arr:
            both_num += 1
    print(len(first_arr) + len(second_arr) - 2 * both_num)


if __name__ == "__main__":
    main()
