import sys


def main():
    input_num = int(sys.stdin.readline().rstrip())
    first_num = 0
    second_num = 1
    for _ in range(1, input_num + 1):
        third_num = (first_num + second_num) % 15746
        first_num = second_num
        second_num = third_num
    print(third_num)


if __name__ == "__main__":
    main()
