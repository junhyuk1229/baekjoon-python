import sys
from collections import deque


def order_arr(build_order, build_left, build_time, end_num):
    build_time_total = [0] * len(build_left)
    build_queue = deque()
    for i in range(len(build_left)):
        if build_left[i] == 0 and i != 0:
            build_queue.append(i)
    while build_queue:
        temp_build = build_queue.popleft()
        build_time_total[temp_build] += build_time[temp_build - 1]
        for index in build_order[temp_build]:
            build_left[index] -= 1
            if build_left[index] == 0:
                build_queue.append(index)
            if build_time_total[index] < build_time_total[temp_build]:
                build_time_total[index] = build_time_total[temp_build]
    return build_time_total[end_num]


def main():
    case_num = int(sys.stdin.readline().rstrip())
    for _ in range(case_num):
        build_num, build_order = map(int, sys.stdin.readline().rstrip().split(sep=' '))
        build_time = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
        build_order_arr = {i + 1: [] for i in range(build_num)}
        build_left = [0] * (build_num + 1)
        for _ in range(build_order):
            first_build, second_build = map(int, sys.stdin.readline().rstrip().split(sep=' '))
            build_order_arr[first_build].append(second_build)
            build_left[second_build] += 1
        final_build = int(sys.stdin.readline().rstrip())
        print(order_arr(build_order_arr, build_left, build_time, final_build))


if __name__ == "__main__":
    main()
