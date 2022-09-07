import sys

def main():
    firstCost, perCost, perGain = map(int, sys.stdin.readline().split(sep=" "))
    if perCost >= perGain:
        print(-1)
    else:
        print((firstCost // (perGain - perCost)) + 1)


if __name__ == "__main__":
    main()