RANGENUM = 10000
resultArr = []

for i in range(RANGENUM):
    resultArr.append(0)

for i in range(1, len(resultArr) + 1):
    tempI = i
    nextNum = tempI
    while tempI > 0:
        nextNum += tempI % 10
        tempI //= 10
    if nextNum <= 10000:
        resultArr[nextNum - 1] = 1
    if resultArr[i - 1] == 0:
        print(i)