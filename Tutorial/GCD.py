def GCD(first_num, second_num):
    while second_num != 0:
        rem_num = first_num % second_num
        first_num = second_num
        second_num = rem_num
    return first_num