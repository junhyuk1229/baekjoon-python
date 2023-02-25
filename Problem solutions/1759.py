import sys


VOWEL_LIST = ['a', 'e', 'i', 'o', 'u']


def recur_print_pass(input_list: list, remain_num: int, start_index: int, output_str='', vowel_num=0, cons_num=0) -> None:
    if remain_num == 0:
        # Check number of vowels and consonants
        if vowel_num < 1 or cons_num < 2:
            return
        print(output_str)
        return

    # Loop all values
    for temp_index, temp_val in enumerate(input_list[start_index:len(input_list) - remain_num + 1]):
        # If value added is a vowel
        if temp_val in VOWEL_LIST:
            recur_print_pass(input_list, remain_num - 1, start_index + temp_index + 1, output_str + temp_val,
                             vowel_num + 1, cons_num)
        # If value added is not a vowel
        else:
            recur_print_pass(input_list, remain_num - 1, start_index + temp_index + 1, output_str + temp_val,
                             vowel_num, cons_num + 1)
    return


def main() -> None:
    # Get data input
    pass_len, input_len = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    input_list = list(sys.stdin.readline().rstrip().split(sep=' '))
    # Sort input list to print
    input_list.sort()

    # Check input
    '''
    print("password length: {0}".format(pass_len))
    print("input list length: {0}".format(input_len))
    print("sorted list: {0}".format(input_list))
    '''

    # Use Recursion to get output
    recur_print_pass(input_list, pass_len, 0)

    return


if __name__ == '__main__':
    main()
