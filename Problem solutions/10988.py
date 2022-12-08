import sys


def main():
    input_word = sys.stdin.readline().rstrip()
    is_palin = 1
    for i in range(len(input_word) // 2):
        if input_word[i] != input_word[len(input_word) - i - 1]:
            is_palin = 0
            break
    print(is_palin)


if __name__ == "__main__":
    main()
