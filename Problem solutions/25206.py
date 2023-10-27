import sys


TOTALCLASS = 20
GRADEDICT = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
}


def main() -> None:
    total_credit = 0
    total_grade = 0

    for _ in range(TOTALCLASS):
        _, credit, grade = sys.stdin.readline().rstrip().split(sep=' ')

        if grade == 'P':
            continue

        grade = GRADEDICT[grade]

        total_credit += int(credit[0])
        total_grade += int(credit[0]) * grade

    print(total_grade / total_credit)


if __name__ == '__main__':
    main()
