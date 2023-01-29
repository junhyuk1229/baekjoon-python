import sys


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    if n // 2 < m:
        m = n - m
    output_num = 1
    div_num = 1
    for temp_num in range(1, m + 1):
        div_num *= temp_num
        output_num *= n - temp_num + 1
    print(output_num // div_num)
    return


if __name__ == "__main__":
    main()
