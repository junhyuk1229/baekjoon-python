import sys


def main():
    round_num = int(sys.stdin.readline().rstrip())
    first_score = second_score = 100
    for _ in range(round_num):
        first_die, second_die = map(int, sys.stdin.readline().split(sep=' '))
        if first_die < second_die:
            first_score -= second_die
        elif second_die < first_die:
            second_score -= first_die
    print(f"{first_score}\n{second_score}")


if __name__ == "__main__":
    main()
