import sys


def check_six_three(input_num):
    count_six = 0
    while input_num > 0 :
        if input_num % 10 == 6:
            count_six += 1
        else:
            count_six = 0
        if count_six == 3:
            return True
        input_num //= 10
    return False



def main():
    check_num = 666
    count_num = 1
    obj_num = int(sys.stdin.readline().rstrip())
    while obj_num != count_num:
        check_num += 1
        if check_six_three(check_num):
            count_num += 1
    print(check_num)


if __name__ == "__main__":
    main()
