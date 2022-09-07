import sys


def main():
    totalCost = int(sys.stdin.readline())
    totalAmount = int(sys.stdin.readline())
    for i in range(totalAmount):
        itemCost, itemAmount = map(int, sys.stdin.readline().split(' '))
        totalCost -= itemCost * itemAmount
    if totalCost == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()