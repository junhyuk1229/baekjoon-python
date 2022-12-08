import sys


def main():
    input_grade = sys.stdin.readline().rstrip()
    output_num = 0.0
    if input_grade == 'F':
        print(0.0)
        return
    if input_grade[1] == '-':
        output_num -= 0.3
    elif input_grade[1] == '+':
        output_num += 0.3
    output_num += 69 - ord(input_grade[0])
    print(f"{output_num:.1f}")


if __name__ == "__main__":
    main()
