import sys


def main():
    point_num = int(sys.stdin.readline().rstrip())
    output_arr = [0] * 5
    for _ in range(point_num):
        x_num, y_num = map(int, sys.stdin.readline().split(sep=' '))
        if x_num * y_num == 0:
            output_arr[4] += 1
        elif x_num > 0 and y_num > 0:
            output_arr[0] += 1
        elif x_num > 0 and y_num < 0:
            output_arr[3] += 1
        elif y_num > 0:
            output_arr[1] += 1
        else:
            output_arr[2] += 1
    output_str = ["Q1: ", "Q2: ", "Q3: ", "Q4: ", "AXIS: "]
    for index_num in range(5):
        print(f"{output_str[index_num]}{output_arr[index_num]}")


if __name__ == "__main__":
    main()
