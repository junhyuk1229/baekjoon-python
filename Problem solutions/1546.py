import sys

count = int(sys.stdin.readline().rstrip())
scoreList = list(map(int, sys.stdin.readline().split()))
maxScore = 0
totalScore = 0

for score in scoreList:
    if maxScore < score:
        maxScore = score
    totalScore += score

print(totalScore / len(scoreList) / maxScore * 100)