import sys

loopCount = int(sys.stdin.readline().rstrip())

for _ in range(loopCount):
    cpyTimes, strArr = sys.stdin.readline().split(sep=' ')
    for i in range(len(strArr) - 1):
        for j in range(int(cpyTimes)):
            print(strArr[i], end='')
    print()