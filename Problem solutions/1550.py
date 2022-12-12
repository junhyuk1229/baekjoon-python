import sys


def hex_to_dec(input_string):
    return_num = 0
    for i in input_string:
        return_num *= 16
        if i >= 'A':
            i = ord(i) - ord('A') + 10
        else:
            i = ord(i) - ord('0')
        return_num += i
    return return_num


def main():
    input_hex = sys.stdin.readline().rstrip()
    print(hex_to_dec(input_hex))


if __name__ == "__main__":
    main()
