import sys, math


def slope(first_point, second_point):
    x_dist = first_point[0] - second_point[0]
    y_dist = first_point[1] - second_point[1]
    if y_dist == 0:
        return math.inf
    return x_dist / y_dist


def dist(first_point, second_point):
    x_dist = first_point[0] - second_point[0]
    y_dist = first_point[1] - second_point[1]
    return math.sqrt((x_dist ** 2) + (y_dist ** 2))


def main():
    input_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))

    if slope(input_list[:2], input_list[2:4]) == slope(input_list[:2], input_list[4:]):
        print(-1)
        return

    min_len = math.inf
    max_len = 0.0

    temp_dist = dist(input_list[:2], input_list[2:4])
    min_len = min(min_len, temp_dist)
    max_len = max(max_len, temp_dist)
    temp_dist = dist(input_list[:2], input_list[4:])
    min_len = min(min_len, temp_dist)
    max_len = max(max_len, temp_dist)
    temp_dist = dist(input_list[2:4], input_list[4:])
    min_len = min(min_len, temp_dist)
    max_len = max(max_len, temp_dist)

    print(2 * (max_len - min_len))
    return


if __name__ == '__main__':
    main()
