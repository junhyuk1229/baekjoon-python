import sys


def main():
    input_len, query_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    input_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    sum_arr = [0 for _ in range(input_len + 1)]
    for i in range(input_len):
        sum_arr[i + 1] = sum_arr[i] + input_arr[i]
    for _ in range(query_num):
        first_num, last_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
        print(sum_arr[last_num] - sum_arr[first_num - 1])


if __name__ == "__main__":
    main()
