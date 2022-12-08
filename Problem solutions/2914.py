import sys


def main():
    song_num, avg_num = map(int, sys.stdin.readline().split(sep=' '))
    print(song_num * (avg_num-1) + 1)


if __name__ == "__main__":
    main()