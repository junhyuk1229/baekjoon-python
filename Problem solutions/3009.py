import sys


def main():
    points = []
    for _ in range(3):
        points.append(list(map(int, sys.stdin.readline().split(sep=' '))))
    for i in range(2):
        if points[0][i] == points[1][i]:
            print(points[2][i], end=' ')
        else:
            print(points[0][i] + points[1][i] - points[2][i], end=' ')


if __name__ == "__main__":
    main()
