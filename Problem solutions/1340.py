import sys


DAY_LIST = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAY_LEAP = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DATE_NAME = {
                "January": 0, "February": 1, "March": 2, "April": 3, "May": 4, "June": 5,
                "July": 6, "August": 7, "September": 8, "October": 9, "November": 10, "December": 11
            }


def main():
    input_list = sys.stdin.readline().rstrip().split(sep=' ')
    is_leap = False

    year_num = int(input_list[2])
    if year_num % 400 == 0 or (year_num % 100 != 0 and year_num % 4 == 0):
        is_leap = True

    check_arr = [0]
    if is_leap:
        for temp_day in DAY_LEAP:
            check_arr.append(check_arr[-1] + temp_day)
    else:
        for temp_day in DAY_LIST:
            check_arr.append(check_arr[-1] + temp_day)

    output_percent = 0.0
    output_percent += (check_arr[DATE_NAME[input_list[0]]] + int(input_list[1][0:2]) - 1) / check_arr[-1]
    output_percent += int(input_list[-1][0:2]) / check_arr[-1] / 24
    output_percent += int(input_list[-1][3:]) / check_arr[-1] / 24 / 60

    print(round(output_percent, 12) * 100)
    return


if __name__ == '__main__':
    main()
