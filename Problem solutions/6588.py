import sys
import math


def checkPrime(inputNum):
    checkNum = 2
    while checkNum <= round(math.sqrt(inputNum)):
        if inputNum % checkNum == 0:
            return False
        checkNum += 1
    return True


def main():
    while True:
        inputNum = int(sys.stdin.readline().rstrip())
        if inputNum == 0:
            break
        tempNum = 3
        while tempNum <= inputNum // 2:
            if checkPrime(tempNum) and checkPrime(inputNum - tempNum):
                print(f"{inputNum} = {tempNum} + {inputNum - tempNum}")
                break
            tempNum += 2
        if tempNum > inputNum // 2:
            print("Goldbach's conjecture is wrong.")


if __name__ == "__main__":
    main()