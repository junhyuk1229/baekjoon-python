import sys


def main():
    list_len = int(sys.stdin.readline().rstrip())
    input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    output_list = []
    max_output_index = -1
    max_output_num = 0
    for temp_index, temp_value in enumerate(input_list):
        output_list.append([])
        for temp_comp_index, temp_comp_value in enumerate(input_list[:temp_index]):
            if temp_value <= temp_comp_value:
                continue
            if len(output_list[temp_index]) < len(output_list[temp_comp_index]):
                output_list[temp_index] = output_list[temp_comp_index].copy()
        output_list[temp_index].append(temp_value)
        if len(output_list[temp_index]) > max_output_num:
            max_output_num = len(output_list[temp_index])
            max_output_index = temp_index
    print(max_output_num)
    print(' '.join(map(str, output_list[max_output_index])))


if __name__ == "__main__":
    main()
