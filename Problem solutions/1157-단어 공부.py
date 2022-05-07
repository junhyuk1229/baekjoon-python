import sys

inputStr = sys.stdin.readline().rstrip()
searchArr = []

for _ in range(26):
    searchArr.append(0)

for inputChar in inputStr:
    tempIndex = ord(inputChar) - 65
    if tempIndex >= 32:
        tempIndex -= 32
    searchArr[tempIndex] += 1

maxNum = 0

for i in range(26):
    if maxNum < searchArr[i]:
        maxNum = searchArr[i]
        resultChar = i
    elif maxNum == searchArr[i]:
        resultChar = -1

if resultChar == -1:
    print('?')
else:
    print(chr(65 + resultChar))