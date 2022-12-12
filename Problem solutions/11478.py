import sys


def main():
    input_str = sys.stdin.readline().rstrip()
    check_set = set()
    for i in range(len(input_str)):
        for j in range(len(input_str) + 1):
            if i >= j:
                continue
            check_set.add(input_str[i:j])
    print(len(check_set))


if __name__ == "__main__":
    main()
