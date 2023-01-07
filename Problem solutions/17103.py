import sys


MAX_NUM = 1000000


case_num = int(sys.stdin.readline().rstrip())
prime_check_arr = [True] * (MAX_NUM + 1)


# update prime array
for temp_index in range(2, MAX_NUM // 2 + 1):
    if not prime_check_arr[temp_index]:
        continue
    for false_index in range(temp_index * 2, MAX_NUM + 1, temp_index):
        prime_check_arr[false_index] = False


# check for ways to make number with sum of 2 primes
for _ in range(case_num):
    input_num = int(sys.stdin.readline().rstrip())
    if input_num == 4:
        print(1)
        continue
    output_num = 0
    for temp_index in range(3, input_num // 2 + 1, 2):
        if prime_check_arr[temp_index] and prime_check_arr[input_num - temp_index]:
            output_num += 1
    print(output_num)
