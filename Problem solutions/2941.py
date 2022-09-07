import sys

croatyAlph = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]

def main():
    inputStr = sys.stdin.readline().rstrip()
    croatySkip = 0
    i = 0
    while i < len(inputStr) - 1:
        if inputStr[i:i+2] in croatyAlph:
            croatySkip += 1
            i += 1
        elif i < len(inputStr) - 2 and inputStr[i:i+3] == "dz=":
            croatySkip += 2
            i += 2
        i += 1
    print(len(inputStr) - croatySkip)


if __name__ == "__main__":
    main()