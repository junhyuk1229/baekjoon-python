import sys


def main():
    case_num = int(sys.stdin.readline().rstrip())
    for _ in range(case_num):
        uni_name = None
        bottle_num = 0
        uni_num = int(sys.stdin.readline().rstrip())
        for _ in range(uni_num):
            temp_uni, temp_bottle = sys.stdin.readline().rstrip().split(sep=' ')
            if bottle_num < int(temp_bottle):
                bottle_num = int(temp_bottle)
                uni_name = temp_uni
        print(uni_name)


if __name__ == "__main__":
    main()
