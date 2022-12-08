import sys


def main():
    case_num = int(sys.stdin.readline().rstrip())
    for _ in range(case_num):
        non_adv, adv, adv_cost = map(int, sys.stdin.readline().split(sep=' '))
        if non_adv < adv - adv_cost:
            print("advertise")
        elif non_adv == adv - adv_cost:
            print("does not matter")
        else:
            print("do not advertise")


if __name__ == "__main__":
    main()
