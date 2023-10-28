import sys


MAX_SUB = 100000


def main() -> None:
    subject_num, total_work_time = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    output_list = [0] * (MAX_SUB + 1)

    for _ in range(subject_num):
        study_time, point_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))

        for temp_index in range(MAX_SUB, study_time - 1, -1):
            output_list[temp_index] = max(output_list[temp_index], output_list[temp_index - study_time] + point_num)

    print(max(output_list[:total_work_time + 1]))


if __name__ == "__main__":
    main()
