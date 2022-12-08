import sys


def main():
    vote_num = int(sys.stdin.readline().rstrip())
    is_cute = 0
    for _ in range(vote_num):
        is_cute += int(sys.stdin.readline().rstrip()) * 2 - 1
    if is_cute < 0:
        print("Junhee is not cute!")
    else:
        print("Junhee is cute!")


if __name__ == "__main__":
    main()
