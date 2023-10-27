import sys


LINENUM = 5


def main() -> None:
    str_list = []
    max_seq_len = 0

    for _ in range(LINENUM):
        input_str = sys.stdin.readline().rstrip()
        max_seq_len = max(max_seq_len, len(input_str))
        str_list.append(input_str)

    output_str = ''

    for index in range(max_seq_len):
        for temp_str in str_list:
            if len(temp_str) <= index:
                continue
            output_str += temp_str[index]

    print(output_str)


if __name__ == '__main__':
    main()
