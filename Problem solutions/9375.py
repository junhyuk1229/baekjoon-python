import sys


def main():
    case_num = int(sys.stdin.readline().rstrip())
    for _ in range(case_num):
        dict_cloth = dict()
        cloth_num = int(sys.stdin.readline().rstrip())
        for _ in range(cloth_num):
            __, cloth_type = sys.stdin.readline().rstrip().split(sep=' ')
            if cloth_type not in dict_cloth:
                dict_cloth[cloth_type] = 0
            dict_cloth[cloth_type] += 1
        output_num = 0
        for temp_num in dict_cloth.values():
            if output_num == 0:
                output_num = temp_num
            else:
                output_num *= temp_num + 1
                output_num += temp_num
        print(output_num)


if __name__ == "__main__":
    main()
