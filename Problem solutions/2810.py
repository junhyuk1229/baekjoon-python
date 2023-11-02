from collections import Counter
import sys


def main() -> None:
    input_len = int(sys.stdin.readline().rstrip())
    counter_dict = Counter(sys.stdin.readline().rstrip())

    if counter_dict['L'] == 0:
        print(input_len)
        return

    print(input_len - counter_dict['L'] // 2 + 1)

    return


if __name__ == "__main__":
    main()
