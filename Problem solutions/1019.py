import sys


def main() -> None:
    input_num = int(sys.stdin.readline().rstrip())

    expo_num = 1

    while input_num >= 10 ** expo_num:
        expo_num += 1

    output_list = [0] * 10

    for temp_expo in range(expo_num):
        output_list[0] -= 10 ** temp_expo

    for temp_expo in range(expo_num - 1, -1, -1):
        temp_num = input_num // (10 ** temp_expo)

        for i in range(10):
            output_list[i] += int(temp_num * temp_expo * 10 ** (temp_expo - 1))

        for i in range(temp_num):
            output_list[i] += 10 ** temp_expo

        output_list[temp_num] += input_num % 10 ** temp_expo + 1

        input_num %= 10 ** temp_expo

    print(' '.join(map(str, output_list)))

    return


if __name__ == '__main__':
    main()
