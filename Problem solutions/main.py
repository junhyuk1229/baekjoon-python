import sys


def main():
    num_length = int(sys.stdin.readline().rstrip())
    num_list = []
    for i in range(num_length):
        temp_one, temp_two = map(int, sys.stdin.readline().split(sep = ' '))
        num_list.append([temp_one, temp_two])


if __name__ == "__main__":
    main()
