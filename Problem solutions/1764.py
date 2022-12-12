import sys


def main():
    notseen_people = set()
    output_arr = []
    notseen_num, notheard_num = map(int, sys.stdin.readline().split(sep=' '))
    for _ in range(notseen_num):
        notseen_people.add(sys.stdin.readline().rstrip())
    for _ in range(notheard_num):
        temp_str = sys.stdin.readline().rstrip()
        if temp_str in notseen_people:
            output_arr.append(temp_str)
    print(len(output_arr))
    output_arr.sort()
    for temp_char in output_arr:
        print(temp_char)


if __name__ == "__main__":
    main()
