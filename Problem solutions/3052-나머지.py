import sys

remArr = []
for i in range(42):
    remArr.append(0)

for i in range(10):
    remArr[int(sys.stdin.readline().rstrip()) % 42] += 1

uniqueNum = 0
for i in remArr:
    if i != 0:
        uniqueNum += 1

print(uniqueNum)