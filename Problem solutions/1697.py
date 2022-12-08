import sys
from collections import deque


MAX_LEN = 10 ** 5


def bfsSearch(fromNum, toNum):
    checkQueue = deque([toNum])
    distArr = [0] * (MAX_LEN + 1)
    distArr[toNum] = 1
    while distArr[fromNum] == 0:
        temp = checkQueue.popleft()
        checkNums = [temp - 1, temp + 1]
        if temp % 2 == 0:
            checkNums.append(temp // 2)
        for check in checkNums:
            if check < 0 or check > MAX_LEN or distArr[check] != 0:
                continue
            distArr[check] = distArr[temp] + 1
            checkQueue.append(check)
    return distArr[fromNum]


def main():
    fromNum, toNum = map(int, sys.stdin.readline().split(sep=' '))
    print(bfsSearch(fromNum, toNum) - 1)



if __name__ == "__main__":
    main()