import sys


def main():
    height_size, width_size = map(int, sys.stdin.readline().split(sep=' '))
    output_arr = [[0]] * height_size
    for index in range(height_size):
        output_arr[index] = list(map(int, sys.stdin.readline().split(sep=' ')))
    for index in range(height_size):
        temp_arr = list(map(int, sys.stdin.readline().split(sep=' ')))
        for j in range(width_size):
            output_arr[index][j] += temp_arr[j]
            print(output_arr[index][j], end=' ')
        print()


if __name__ == "__main__":
    main()
