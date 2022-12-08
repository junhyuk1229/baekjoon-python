import sys


def main():
    inputArr = list(map(int, sys.stdin.readline().split(sep=' ')))
    inputArr.sort()
    print(inputArr[1])


if __name__ == "__main__":
    main()