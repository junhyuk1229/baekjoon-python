import sys


def main():
    fruit_per_meter = int(sys.stdin.readline().rstrip())
    counter_clock_arr = []
    for _ in range(6):
        counter_clock_arr.append(list(map(int, sys.stdin.readline().rstrip().split(sep=' '))))
    for index in range(6):
        if counter_clock_arr[index][0] == counter_clock_arr[(index + 2) % 6][0]:
            first_len = counter_clock_arr[index][1] + counter_clock_arr[(index + 2) % 6][1]
            if counter_clock_arr[index + 1][0] == counter_clock_arr[(index + 3) % 6][0]:
                second_len = counter_clock_arr[index + 1][1] + counter_clock_arr[(index + 3) % 6][1]
                first_small = counter_clock_arr[(index + 2) % 6][1]
                second_small = counter_clock_arr[index + 1][1]
            else:
                second_len = counter_clock_arr[(index - 1) % 6][1] + counter_clock_arr[(index + 1) % 6][1]
                first_small = counter_clock_arr[index][1]
                second_small = counter_clock_arr[(index + 1) % 6][1]
            break
    print((first_len * second_len - first_small * second_small) * fruit_per_meter)


if __name__ == "__main__":
    main()
