import sys


def main() -> None:
    first_deg = int(sys.stdin.readline().rstrip())
    second_deg = int(sys.stdin.readline().rstrip())
    third_deg = int(sys.stdin.readline().rstrip())

    if first_deg + second_deg + third_deg != 180:
        print("Error")
        return

    if first_deg == second_deg == third_deg:
        print("Equilateral")
        return

    if (first_deg == second_deg) or (second_deg == third_deg) or (third_deg == first_deg):
        print("Isosceles")
        return

    print("Scalene")
    return


if __name__ == '__main__':
    main()
