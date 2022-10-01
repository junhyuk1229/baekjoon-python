import sys


def palindromeCheck(inputStr, recurNum):
    if len(inputStr) < 2:
        return [1, recurNum]
    if inputStr[0] != inputStr[-1]:
        return [0, recurNum]
    return palindromeCheck(inputStr[1:-1], recurNum + 1)


def main():
    repNum = int(sys.stdin.readline().rstrip())
    for i in range(repNum):
        inputStr = sys.stdin.readline().rstrip()

        checkNum = palindromeCheck(inputStr, 1)

        print(' '.join(map(str, checkNum)))

if __name__ == "__main__":
    main()