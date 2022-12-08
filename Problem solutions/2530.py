import sys


def main():
    hour_num, min_num, sec_num = map(int, sys.stdin.readline().split(sep=' '))
    cook_time = int(sys.stdin.readline().rstrip())

    sec_num += cook_time % 60
    if sec_num >= 60:
        sec_num -= 60
        min_num += 1
    min_num += (cook_time // 60) % 60
    if min_num >= 60:
        min_num -= 60
        hour_num += 1
    hour_num += cook_time // 3600
    if hour_num >= 24:
        hour_num -= (hour_num//24) * 24
    print(" ".join(map(str, [hour_num, min_num, sec_num])))


if __name__ == "__main__":
    main()
