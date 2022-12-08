import sys


def main():
    total_sum = 0
    for _ in range(5):
        input_num = int(sys.stdin.readline().rstrip())
        if input_num < 40:
            total_sum += 40
        else:
            total_sum += input_num
    print(total_sum // 5)


if __name__ == "__main__":
    main()
