import sys


def GCD(first_num, second_num):
    while second_num != 0:
        rem_num = first_num % second_num
        first_num = second_num
        second_num = rem_num
    return first_num



def print_factor(input_num):
    factor = 2
    output_list = list([input_num])
    while factor * factor <= input_num:
        if input_num % factor == 0:
            output_list.append(factor)
            if factor * factor != input_num:
                output_list.append(input_num // factor)
        factor += 1
    output_list.sort()
    for temp_num in output_list:
        print(temp_num, end=' ')


def main():
    input_num = int(sys.stdin.readline().rstrip())
    input_arr = [0] * input_num
    diff_arr = [0] * input_num
    for index_num in range(input_num):
        input_arr[index_num] = int(sys.stdin.readline().rstrip())
    for index_num in range(input_num):
        diff_arr[index_num] = input_arr[index_num] - input_arr[(index_num + 1) % input_num]
        if diff_arr[index_num] < 0:
            diff_arr[index_num] = 0 - diff_arr[index_num]
    target_num = diff_arr[0]
    for index_num in range(input_num - 1):
        target_num = GCD(target_num, diff_arr[index_num + 1])
    print_factor(target_num)


if __name__ == "__main__":
    main()
