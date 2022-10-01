import sys


def main():
    repeatTimes = int(sys.stdin.readline().rstrip())
    for i in range(repeatTimes):
        floorNum = int(sys.stdin.readline().rstrip())
        partNum = int(sys.stdin.readline().rstrip())
        resultNum = 1
        indexNum = 1
        while indexNum < partNum:
            resultNum *= floorNum + partNum - indexNum + 1
            indexNum += 1
        indexNum = 1
        while indexNum < partNum:
            resultNum //= indexNum
            indexNum += 1
        print(resultNum)


if __name__ == "__main__":
    main()