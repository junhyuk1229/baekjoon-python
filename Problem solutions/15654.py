import sys


def recur_print(input_list, input_map, output_len, output_list):
    if len(output_list) == output_len:
        print(' '.join(map(str, output_list)))
        return
    for temp_index, temp_num in enumerate(input_list):
        if input_map[temp_index]:
            continue
        input_map[temp_index] = True
        output_list.append(temp_num)
        recur_print(input_list, input_map, output_len, output_list)
        output_list.pop()
        input_map[temp_index] = False
    return


def main():
    input_len, output_len = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    input_list.sort()
    input_map = [False] * input_len

    recur_print(input_list, input_map, output_len, [])
    return


if __name__ == "__main__":
    main()
