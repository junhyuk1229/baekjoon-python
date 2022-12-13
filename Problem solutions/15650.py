import sys


def repeat_print(input_set, max_num, num_num):
    if num_num == 0:
        print(' '.join(map(str, input_set)))
        return
    if len(input_set) == 0:
        start_num = 1
    else:
        start_num = input_set[-1]
    for temp_num in range(start_num, max_num + 1):
        if temp_num not in input_set:
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
