import sys


def merge_sort(input_arr):
    if len(input_arr) == 1:
        return input_arr
    mid_index = len(input_arr) // 2
    first_arr = merge_sort(input_arr[0:mid_index])
    second_arr = merge_sort(input_arr[mid_index:])
    result_arr = []
    first_index = second_index = 0
    while (first_index < len(first_arr)) and (second_index < len(second_arr)):
        if first_arr[first_index] < second_arr[second_index]:
            result_arr.append(first_arr[first_index])
            first_index += 1
        else:
            result_arr.append(second_arr[second_index])
            second_index += 1
    if second_index == len(second_arr):
        while first_index < len(first_arr):
            result_arr.append(first_arr[first_index])
            first_index += 1
    else:
        while second_index < len(second_arr):
            result_arr.append(second_arr[second_index])
            second_index += 1
    return result_arr


def search_half(input_arr, input_num):
    start_index = 0
    middle_index = (len(input_arr) - 1) // 2
    end_index = len(input_arr) - 1
    while start_index <= end_index:
        if input_arr[middle_index] == input_num:
            return True
        if input_arr[middle_index] < input_num:
            start_index = middle_index + 1
        else:
            end_index = middle_index - 1
        middle_index = (start_index + end_index) // 2
    return False


def main():
    input_num = int(sys.stdin.readline().rstrip())
    input_arr = set(map(int, sys.stdin.readline().split(sep=' ')))
    answer_num = int(sys.stdin.readline().rstrip())
    answer_arr = list(map(int, sys.stdin.readline().split(sep=' ')))
    input_arr = merge_sort(input_arr)
    for temp_num in answer_arr:
        if search_half(input_arr, temp_num):
            print("1", end=' ')
        else:
            print("0", end=' ')


if __name__ == "__main__":
    main()
