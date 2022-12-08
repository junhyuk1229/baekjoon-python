import sys


def main():
    test_case = int(sys.stdin.readline().rstrip())
    for _ in range(test_case):
        yon_score = kor_score = 0
        for _ in range(9):
            yon_temp, kor_temp = map(int, sys.stdin.readline().split(sep=' '))
            yon_score += yon_temp
            kor_score += kor_temp
        if yon_score > kor_score:
            print("Yonsei")
        elif kor_score > yon_score:
            print("Korea")
        else:
            print("Draw")



if __name__ == "__main__":
    main()
