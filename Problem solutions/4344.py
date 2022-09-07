import sys

testCount = int(sys.stdin.readline().rstrip())

for i in range(testCount):
    studentCountScore = list(map(int, sys.stdin.readline().split()))
    totalScore = 0
    for j in range(1, studentCountScore[0] + 1):
        totalScore += studentCountScore[j]
    totalScore /= studentCountScore[0]
    aboveAvg = 0
    for j in range(1, studentCountScore[0] + 1):
        if totalScore < studentCountScore[j]:
            aboveAvg += 1
    print(format(aboveAvg / studentCountScore[0] * 100, ".3f"), '%', sep='')