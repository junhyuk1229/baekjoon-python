import sys


def main():
    input_len = int(sys.stdin.readline().rstrip())
    paint_cost = [0 for _ in range(3)]
    for _ in range(input_len):
        temp_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
        temp_list[0] += min(paint_cost[1], paint_cost[2])
        temp_list[1] += min(paint_cost[0], paint_cost[2])
        temp_list[2] += min(paint_cost[0], paint_cost[1])
        paint_cost = temp_list
    print(min(paint_cost))


if __name__ == "__main__":
    main()
