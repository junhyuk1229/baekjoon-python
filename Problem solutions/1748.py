import sys


def main() -> None:
    input_num = int(sys.stdin.readline().rstrip())
    place_num = 1
    output_num = 0

    while pow(10, place_num) <= input_num:
        output_num += 9 * pow(10, place_num - 1) * place_num
        place_num += 1

    output_num += (input_num - pow(10, place_num - 1) + 1) * place_num

    print(output_num)

    return


if __name__ == "__main__":
  main()
