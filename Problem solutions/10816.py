import sys
from collections import Counter


def main():
    input_num = int(sys.stdin.readline().rstrip())
    input_arr = Counter(list(map(int, sys.stdin.readline().split(sep=' '))))
    output_num = int(sys.stdin.readline().rstrip())
    output_arr = list(map(int, sys.stdin.readline().split(sep=' ')))
    for temp_num in output_arr:
        print(input_arr[temp_num], end=' ')


if __name__ == "__main__":
    main()
