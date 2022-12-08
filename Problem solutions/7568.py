import sys


def main():
    people_num = int(sys.stdin.readline().rstrip())
    weight_arr = [0] * people_num
    height_arr = [0] * people_num
    for temp_num in range(people_num):
        weight_arr[temp_num], height_arr[temp_num] = map(int, sys.stdin.readline().split(sep=' '))
    for check_index in range(people_num):
        output_num = 1
        for temp_index in range(people_num):
            if weight_arr[check_index] < weight_arr[temp_index] and height_arr[check_index] < height_arr[temp_index]:
                output_num += 1
        print(f"{output_num}", end=' ')


if __name__ == "__main__":
    main()
