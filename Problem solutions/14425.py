import sys


def main():
    input_num, check_num = map(int, sys.stdin.readline().split(sep=' '))
    input_arr = []
    for _ in range(input_num):
        input_arr.append(sys.stdin.readline().rstrip())
    output_num = 0
    input_arr = set(input_arr)
    for _ in range(check_num):
        if sys.stdin.readline().rstrip() in input_arr:
            output_num += 1
    print(output_num)


if __name__ == "__main__":
    main()
