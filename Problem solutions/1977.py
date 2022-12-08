import sys
import math


def main():
    min_num = math.ceil(math.sqrt(int(sys.stdin.readline().rstrip())))
    max_num = int(sys.stdin.readline().rstrip())
    min_output = min_num
    total_sum = 0
    while min_num ** 2 <= max_num:
        total_sum += min_num ** 2
        min_num += 1
    if total_sum:
        print(f"{total_sum}\n{min_output ** 2}")
    else:
        print(-1)


if __name__ == "__main__":
    main()
