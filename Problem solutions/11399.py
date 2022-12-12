import sys


def main():
    input_length = int(sys.stdin.readline().rstrip())
    input_arr = list(map(int, sys.stdin.readline().split(sep=' ')))
    input_arr.sort()
    total_num = 0
    for temp_num in input_arr:
        total_num += temp_num * input_length
        input_length -= 1
    print(total_num)


if __name__ == "__main__":
    main()
