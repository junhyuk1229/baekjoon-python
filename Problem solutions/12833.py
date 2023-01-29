import sys


def main():
    input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    output_num = input_list[0]
    if input_list[2] % 2 == 1:
        output_num ^= input_list[1]
    print(output_num)
    return


if __name__ == "__main__":
    main()
