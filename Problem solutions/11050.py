import sys


def double(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return double(n - 1, k) + double(n - 1, k - 1)


def main():
    n, k = map(int, sys.stdin.readline().split(sep=' '))
    print(double(n, k))


if __name__ == "__main__":
    main()
