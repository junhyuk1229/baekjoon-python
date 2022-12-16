import sys


def main():
    input_len = int(sys.stdin.readline().rstrip())
    input_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    curr_max = input_arr[0]
    con_max = [0 for _ in range(input_len)]
    con_max[0] = input_arr[0]
    for temp_index, temp_num in enumerate(input_arr[1::]):
        con_max[temp_index + 1] = max(temp_num, con_max[temp_index] + temp_num)
        curr_max = max(curr_max, con_max[temp_index + 1])
    print(curr_max)


if __name__ == "__main__":
    main()
