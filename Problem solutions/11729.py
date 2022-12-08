import sys


def hinoiTower(towerHeight, fromPlace, toPlace):
    if towerHeight == 1:
        print(fromPlace, toPlace)
        return
    hinoiTower(towerHeight - 1, fromPlace, 6 - fromPlace - toPlace)
    print(fromPlace, toPlace)
    hinoiTower(towerHeight - 1, 6 - fromPlace - toPlace, toPlace)


def main():
    inputNum = int(sys.stdin.readline().rstrip())

    print(2 ** inputNum - 1)
    hinoiTower(inputNum, 1, 3)

if __name__ == "__main__":
    main()