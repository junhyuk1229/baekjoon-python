import sys


def main():
    input_str = sys.stdin.readline().rstrip()
    output_str = None

    for first_index in range(len(input_str) - 2):
        for second_index in range(first_index + 1, len(input_str) - 1):
            temp_str = input_str[first_index::-1]
            temp_str += input_str[second_index:first_index:-1]
            temp_str += input_str[:second_index:-1]
            if output_str is None or temp_str < output_str:
                output_str = temp_str

    print(output_str)
    return


if __name__ == '__main__':
    main()
