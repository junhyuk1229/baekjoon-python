import sys, math


def main():
    input_len = int(sys.stdin.readline().rstrip())
    input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    left_sum = []
    right_sum = []
    for temp_num in input_list:
        if len(left_sum) == 0:
            left_sum.append(temp_num)
            continue
        if left_sum[-1] > 0:
            left_sum.append(left_sum[-1] + temp_num)
        else:
            left_sum.append(temp_num)
    for temp_num in input_list[::-1]:
        if len(right_sum) == 0:
            right_sum.append(temp_num)
            continue
        if right_sum[-1] > 0:
            right_sum.append(right_sum[-1] + temp_num)
        else:
            right_sum.append(temp_num)
    right_sum = right_sum[::-1]
    max_num = max(max(right_sum), max(left_sum))
    for first_num, second_num in zip(left_sum, right_sum[2:]):
        max_num = max(max_num, first_num + second_num)
    print(max_num)
    return


if __name__ == "__main__":
    main()
