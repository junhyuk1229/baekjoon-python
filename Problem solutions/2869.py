import sys
import math

def main():
    climbNum, fallNum, totalNum = map(int, sys.stdin.readline().split(" "))
    print(math.ceil((totalNum - climbNum) / (climbNum - fallNum)) + 1)


if __name__ == "__main__":
    main()