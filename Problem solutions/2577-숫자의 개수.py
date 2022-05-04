import sys

numArr = []
for i in range(10):
    numArr.append(0)

resultNum = 1
for i in range(3):
    resultNum *= int(sys.stdin.readline().rstrip())

while resultNum > 0:
    numArr[resultNum % 10] += 1
    resultNum //= 10

for i in numArr:
    print(i)