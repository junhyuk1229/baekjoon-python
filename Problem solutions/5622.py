import sys

turnTime = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
inputStr = sys.stdin.readline().rstrip()
totalTime = 0
for tempChar in inputStr:
    totalTime += turnTime[ord(tempChar) - 65]

print(totalTime)