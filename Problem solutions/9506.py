from collections import deque
import sys
import math


def main():
    input_num = int(sys.stdin.readline().rstrip())
    while input_num != -1:
        factor_arr = deque([])
        total_sum = 0
        check_num = math.floor(math.sqrt(input_num))
        if check_num ** 2 == input_num:
            factor_arr.append(check_num)
            total_sum += check_num
        while check_num > 1:
            if input_num % check_num == 0:
                factor_arr.appendleft(check_num)
                factor_arr.append(input_num // check_num)
                total_sum += input_num // check_num + check_num
            check_num -= 1
        if total_sum == input_num - 1:
            print(f"{input_num} = 1", end='')
            while factor_arr:
                print(f" + {factor_arr.popleft()}", end='')
            print()
        else:
            print(f"{input_num} is NOT perfect.")
        input_num = int(sys.stdin.readline().rstrip())


if __name__ == "__main__":
    main()
