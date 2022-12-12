import sys


def factorial(input_int):
    output_int = 1
    for temp_num in range(input_int):
        output_int *= (temp_num + 1)
    return output_int


def main():
    n, k = map(int, sys.stdin.readline().split(sep=' '))
    print((factorial(n) // factorial(k) // factorial(n - k)) % 10007)


if __name__ == "__main__":
    main()
