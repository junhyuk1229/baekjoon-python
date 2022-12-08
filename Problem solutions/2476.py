import sys


def main():
    case_num = int(sys.stdin.readline().rstrip())
    max_money = 0
    for _ in range(case_num):
        input_arr = list(map(int, sys.stdin.readline().split(sep=' ')))
        input_arr.sort()
        if input_arr[0] == input_arr[1] == input_arr[2]:
            temp_money = 10000 + 1000 * input_arr[1]
        elif input_arr[0] == input_arr[1] or input_arr[1] == input_arr[2]:
            temp_money = 1000 + 100 * input_arr[1]
        else:
            temp_money = 100 * input_arr[2]
        if max_money < temp_money:
            max_money = temp_money
    print(max_money)


if __name__ == "__main__":
    main()