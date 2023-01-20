import sys


MAXNUM = 9901


def main():
    cage_len = int(sys.stdin.readline().rstrip())
    output_arr = [1, 2]
    for _ in range(cage_len):
        zero_num = sum(output_arr) % MAXNUM
        one_num = zero_num + output_arr[0] % MAXNUM
        output_arr = [zero_num, one_num]
    print(output_arr[0])


if __name__ == "__main__":
    main()
