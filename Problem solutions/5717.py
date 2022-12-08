import sys


def main():
    boy_num, girl_num = map(int, sys.stdin.readline().split(sep=' '))
    while not(boy_num == 0 and girl_num == 0):
        print(boy_num + girl_num)
        boy_num, girl_num = map(int, sys.stdin.readline().split(sep=' '))


if __name__ == "__main__":
    main()
