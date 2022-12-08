import sys


def main():
    building_num = int(sys.stdin.readline())
    building_arr = list(map(int, sys.stdin.readline().split(sep=' ')))
    max_output = 0
    for index in range(building_num):
        line_max = None
        temp_output = 0
        for left_index in range(index):
            line_temp = (building_arr[index] - building_arr[index - left_index - 1]) / (left_index + 1)
            if line_max is None or line_temp < line_max:
                line_max = line_temp
                temp_output += 1
        line_max = None
        for right_index in range(building_num - index - 1):
            line_temp = (building_arr[right_index + index + 1] - building_arr[index]) / (right_index + 1)
            if line_max is None or line_temp > line_max:
                line_max = line_temp
                temp_output += 1
        if temp_output > max_output:
            max_output = temp_output
    print(max_output)


if __name__ == "__main__":
    main()
