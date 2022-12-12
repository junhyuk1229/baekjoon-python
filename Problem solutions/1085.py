import sys


def main():
    person_x, person_y, rect_x, rect_y = map(int, sys.stdin.readline().split(sep=' '))
    output_num = person_x
    if output_num > person_y:
        output_num = person_y
    if output_num > rect_x - person_x:
        output_num = rect_x - person_x
    if output_num > rect_y - person_y:
        output_num = rect_y - person_y
    print(output_num)


if __name__ == "__main__":
    main()
