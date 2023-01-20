import sys


def main():
    case_num = int(sys.stdin.readline().rstrip())
    for _ in range(case_num):
        stamp_len = int(sys.stdin.readline().rstrip())
        first_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
        second_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
        last_last_max = 0
        last_list = [0, 0]
        for first_num, second_num in zip(first_list, second_list):
            temp_list = [first_num + max(last_list[1], last_last_max), second_num + max(last_list[0], last_last_max)]
            last_last_max = max(last_list)
            last_list = temp_list
        print(max(last_list))


if __name__ == "__main__":
    main()
