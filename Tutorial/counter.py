def counter(input_arr):
    output_arr = {}
    for temp_num in input_arr:
        if temp_num not in output_arr:
            output_arr[temp_num] = 0
        output_arr[temp_num] += 1
    return output_arr