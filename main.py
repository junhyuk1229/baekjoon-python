import sys, math


def GCD(first_num, second_num):
    if first_num < second_num:
        first_num, second_num = second_num, first_num
    while second_num:
        temp_num = first_num % second_num
        first_num = second_num
        second_num = temp_num
    return first_num


def LCM(first_num, second_num):
    return first_num * second_num // GCD(first_num, second_num)


def solution(arrayA, arrayB):
    first_GCD = arrayA[0]
    first_LCM = arrayA[0]
    for temp_num in arrayA[1:]:
        first_GCD = GCD(first_GCD, temp_num)
        first_LCM = LCM(first_LCM, temp_num)
    second_GCD = arrayB[0]
    second_LCM = arrayA[0]
    for temp_num in arrayB[1:]:
        second_GCD = GCD(second_GCD, temp_num)
        second_LCM = LCM(second_LCM, temp_num)
    first_GCD = first_GCD // GCD(first_GCD, second_LCM)
    second_GCD = second_GCD // GCD(second_GCD, first_LCM)
    if first_GCD == 1 and second_GCD == 1:
        return 0
    return max(first_GCD, second_GCD)



print(solution([10, 17], [5, 20]))
