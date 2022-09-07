import sys

countLine = int(sys.stdin.readline().rstrip())

for i in range(countLine):
    inputLine = sys.stdin.readline()
    score = 0
    oCount = 0
    for letterIndex in inputLine:
        if letterIndex == 'O':
            oCount += 1
        else:
            oCount = 0
        score += oCount
    print(score)