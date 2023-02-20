import sys


def main():
    input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    output_num = 0
    for temp_num in input_list:
        output_num += temp_num
    print(output_num)
    return


if __name__ == '__main__':
    main()
