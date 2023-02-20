import sys


def main():
    input_str = sys.stdin.readline().rstrip()
    output_str = ''
    for temp_char in input_str:
        if temp_char.isupper():
            output_str += temp_char.lower()
        else:
            output_str += temp_char.upper()
    print(output_str)
    return


if __name__ == '__main__':
    main()
