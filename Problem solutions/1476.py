import sys


def main() -> None:
    check_num, sun_num, moon_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    check_num -= 1
    while check_num % 28 != sun_num - 1:
        check_num += 15
    while check_num % 19 != moon_num - 1:
        check_num += (28 * 15)
    print(check_num + 1)
    return


if __name__ == "__main__":
  main()
