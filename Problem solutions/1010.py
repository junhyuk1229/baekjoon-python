import sys


def factorial(input_int):
    output_int = 1
    for temp_num in range(input_int):
        output_int *= (temp_num + 1)
    return output_int


def main():
    case_num = int(sys.stdin.readline().rstrip())
    for _ in range(case_num):
        k, n = map(int, sys.stdin.readline().split(sep=' '))
        print((factorial(n) // factorial(k) // factorial(n - k)))


if __name__ == "__main__":
    main()
