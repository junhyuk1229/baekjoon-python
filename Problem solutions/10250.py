import sys
import math


def main():
    runTimes = int(sys.stdin.readline().rstrip())
    for i in range(runTimes):
        hotelHeight, hotelWidth, customerNum = map(int, sys.stdin.readline().split(sep=" "))
        print(((customerNum - 1) % hotelHeight + 1) * 100 + math.ceil(customerNum / hotelHeight))


if __name__ == "__main__":
    main()