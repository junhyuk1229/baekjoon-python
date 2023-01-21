import sys, math


def main():
    list_len = int(sys.stdin.readline().rstrip())
    input_list = list(map(int, sys.stdin.readline().rstrip()))
    left_sum = [-math.inf] * list_len
    right_sum = [-math.inf] * list_len
    temp_arr = []
    for temp_index in range(list_len):
        temp_arr.append(0)
        for temp_comp_index in range(temp_index):
            break
        temp_arr[temp_index] += input_list[- temp_index - 1]
    return


if __name__ == "__main__":
    main()
