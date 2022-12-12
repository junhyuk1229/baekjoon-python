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