pieceList = [1, 1, 2, 2, 2, 8]

def main():
    inputList = list(map(int, input().split(sep=' ')))
    for i in range(6):
        print(f"{pieceList[i] - inputList[i]} ", end='')

if __name__ == "__main__":
    main()