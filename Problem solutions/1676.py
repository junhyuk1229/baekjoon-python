import sys


def main():
    input_num = int(sys.stdin.readline().rstrip())
    five_num = 5
    output_num = 0
    while five_num <= input_num:
        output_num += input_num // five_num
        five_num *= 5
    print(output_num)

if __name__ == "__main__":
    main()
