import sys


def main():
    arrLen = int(sys.stdin.readline().rstrip())
    inputArr = list(map(int, sys.stdin.readline().split(sep=' ')))
    inputArr.sort()
    print(inputArr[0] * inputArr[arrLen - 1])


if __name__ == "__main__":
    main()