import sys


class Output:
    def __init__(self, output_arr):
        self.output_arr = output_arr
        self.first_check = True

    def update_output(self, input_num):
        if self.first_check:
            self.first_check = False
            self.output_arr[0] = input_num
            self.output_arr[1] = input_num
        else:
            if self.output_arr[0] < input_num:
                self.output_arr[0] = input_num
            if self.output_arr[1] > input_num:
                self.output_arr[1] = input_num


def repeat_func(input_arr, sym_arr, index_num, curr_num, output_class):
    if index_num == len(input_arr):
        output_class.update_output(curr_num)
        return
    for temp_index in range(4):
        if sym_arr[temp_index] == 0:
            continue
        temp_curr_num = curr_num
        if temp_index == 0:
            curr_num += input_arr[index_num]
        elif temp_index == 1:
            curr_num -= input_arr[index_num]
        elif temp_index == 2:
            curr_num *= input_arr[index_num]
        else:
            if curr_num > 0:
                curr_num //= input_arr[index_num]
            else:
                curr_num = - (- curr_num // input_arr[index_num])
        sym_arr[temp_index] -= 1
        repeat_func(input_arr, sym_arr, index_num + 1, curr_num, output_class)
        curr_num = temp_curr_num
        sym_arr[temp_index] += 1



def main():
    input_len = int(sys.stdin.readline().rstrip())
    input_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    sym_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    output_class = Output([0, 0])
    repeat_func(input_arr, sym_arr, 1, input_arr[0], output_class)
    print('\n'.join(map(str, output_class.output_arr)))



if __name__ == "__main__":
    main()
