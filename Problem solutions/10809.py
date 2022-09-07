import sys

inputStr = sys.stdin.readline().rstrip()
charPosArr = []

for i in range(26):
    charPosArr.append(-1)

for arrIndex in range(len(inputStr)):
    if charPosArr[ord(inputStr[arrIndex]) - 97] == -1:
        charPosArr[ord(inputStr[arrIndex]) - 97] = arrIndex

for i in range(26):
    print(charPosArr[i], end=' ')