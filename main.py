import sys


def bubble_sort(input_list, sort_num):
    for sort_index in range(len(input_list) - 1):
        for start_index in range(sort_index + 1):
            if input_list[sort_index - start_index] < input_list[sort_index - start_index + 1]:
                temp_num = input_list[sort_index - start_index]
                input_list[sort_index - start_index] = input_list[sort_index - start_index + 1]
                input_list[sort_index - start_index + 1] = temp_num
                sort_num -= 1
            if sort_num == 0:
                return


def main():
    input_len = int(sys.stdin.readline().rstrip())
    input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    sort_num = int(sys.stdin.readline().rstrip())



    return


if __name__ == '__main__':
    main()
