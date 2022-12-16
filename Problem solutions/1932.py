import sys


def main():
    input_len = int(sys.stdin.readline().rstrip())
    sum_arr = [int(sys.stdin.readline().rstrip())]
    for temp_len in range(1, input_len):
        temp_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
        for i in range(temp_len + 1):
            if i == 0:
                temp_arr[i] += sum_arr[i]
            elif i == temp_len:
                temp_arr[i] += sum_arr[i - 1]
            else:
                temp_arr[i] += max(sum_arr[i], sum_arr[i - 1])
        sum_arr = temp_arr
    print(max(sum_arr))


if __name__ == "__main__":
    main()
