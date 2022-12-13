import sys


def repeat_print(input_set, max_num, num_num):
    if num_num == 0:
        print(' '.join(map(str, input_set)))
        return
    for temp_num in range(1, max_num + 1):
        input_set.append(temp_num)
        repeat_print(input_set, max_num, num_num - 1)
        input_set.pop()
    return


def main():
    max_num, num_num = map(int, sys.stdin.readline().split(sep=' '))
    input_set = list()
    repeat_print(input_set, max_num, num_num)


if __name__ == "__main__":
    main()
