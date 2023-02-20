import sys


def main():
    input_num = int(sys.stdin.readline().rstrip())
    for _ in range(input_num):
        input_str = sys.stdin.readline().rstrip()
        print(input_str[0] + input_str[-1])
    return


if __name__ == '__main__':
    main()
