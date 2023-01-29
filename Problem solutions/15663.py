from collections import Counter
import sys


def print_loop(input_list, output_num, output_list):
    if output_num == len(output_list):
        print(' '.join(map(str, output_list)))
        return

    temp_index = 0
    while temp_index < len(input_list):
        if input_list[temp_index][1] == 0:
            temp_index += 1
            continue
        output_list.append(input_list[temp_index][0])
        input_list[temp_index][1] -= 1
        print_loop(input_list, output_num, output_list)
        input_list[temp_index][1] += 1
        output_list.pop()
        temp_index += 1
    return


def main():
    input_len, output_len = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    input_list = Counter(list(map(int, sys.stdin.readline().rstrip().split(sep=' '))))
    input_list = list(map(list, input_list.items()))
    input_list.sort(key=lambda x: x[0])

    print_loop(input_list, output_len, [])

    return


if __name__ == "__main__":
    main()
