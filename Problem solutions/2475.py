import sys


resultArr = [0, 1, 4, 9, 6, 5, 6, 9, 4, 1]


def main():
    inputArr = list(map(int, sys.stdin.readline().split(sep=' ')))
    outputNum = 0
    for tempNum in inputArr:
        outputNum += resultArr[tempNum]
    print(outputNum % 10)


if __name__ == "__main__":
    main()