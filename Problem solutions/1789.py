import sys
import math


def main():
    input_num = int(sys.stdin.readline().rstrip())
    print(math.floor(math.sqrt(2*input_num + 0.25) - 0.5))



if __name__ == "__main__":
    main()