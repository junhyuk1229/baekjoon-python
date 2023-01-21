import sys


def main():
    input_len = int(sys.stdin.readline().rstrip())
    input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    output_list = [0] * input_len
    for temp_index in range(input_len):
        for temp_comp_index in range(temp_index):
            if input_list[temp_comp_index] >= input_list[temp_index]:
                continue
            output_list[temp_index] = max(output_list[temp_index], output_list[temp_comp_index])
        output_list[temp_index] += input_list[temp_index]
    print(max(output_list))
    return


if __name__ == "__main__":
    main()
