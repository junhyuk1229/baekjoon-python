import sys


def main():
    input_num = int(sys.stdin.readline().rstrip())
    input_arr = list(map(int, sys.stdin.readline().split(sep=' ')))
    search_num = int(sys.stdin.readline().rstrip())
    searched_num = 0
    for temp_int in input_arr:
        if search_num == temp_int:
            searched_num += 1
    print("%d" % searched_num)


if __name__ == "__main__":
    main()
