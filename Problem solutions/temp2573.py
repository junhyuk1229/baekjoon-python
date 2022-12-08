import sys


def main():
    arrLen = int(sys.stdin.readline().rstrip())
    inputArr = list(map(int, sys.stdin.readline().split(sep=' ')))
    sumArr = [[0] * (arrLen - i) for i in range(arrLen)]
    for i in range(arrLen):
        sumArr[0][i] += inputArr[i]
        j = i - 1
        while j >= 0:
            sumArr[i - j][j] = inputArr[i] + sumArr[i - j - 1][j]
            j -= 1
    for i in range(arrLen):
        sumArr[0][i] = 0
        j = i - 1
        while j >= 0:
            if sumArr[i - j][j] != 0:
                sumArr[i - j][j] = 0
            else:
                sumArr[i - j][j] = i - j + 1
            if sumArr[i - j][j] < sumArr[i - j - 1][j]:
                sumArr[i - j][j] = sumArr[i - j - 1][j]
            if sumArr[i - j][j] < sumArr[i - j - 1][j + 1]:
                sumArr[i - j][j] = sumArr[i - j - 1][j + 1]
            j -= 1

    caseNum = int(sys.stdin.readline().rstrip())
    for _ in range(caseNum):
        startNum, endNum = map(int, sys.stdin.readline().split(sep=' '))
        print(sumArr[endNum - startNum][startNum - 1])

if __name__ == "__main__":
    main()