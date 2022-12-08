import sys


def main():
    input_arr = sys.stdin.readline().rstrip()
    last_char = None
    total_height = 0
    for temp_char in input_arr:
        if temp_char == last_char:
            total_height += 5
        else:
            total_height += 10
            last_char = temp_char
    print(total_height)


if __name__ == "__main__":
    main()
