import sys
from collections import Counter, defaultdict


def make_pos(input_counter: Counter, comp_counter: Counter) -> bool:
    for temp_index, temp_val in comp_counter.items():
        if input_counter[temp_index] < temp_val:
            return False
    return True


def main() -> None:
    input_dict = []
    temp_str = sys.stdin.readline().rstrip()
    while temp_str != '-':
        input_dict.append(temp_str)
        temp_str = sys.stdin.readline().rstrip()

    temp_str = sys.stdin.readline().rstrip()
    while temp_str != '#':
        output_dict = defaultdict(lambda: 0)
        temp_counter = Counter(temp_str)

        for temp_dict in input_dict:
            comp_counter = Counter(temp_dict)

            if not make_pos(temp_counter, comp_counter):
                continue

            for temp_index in comp_counter.keys():
                output_dict[temp_index] += 1

        min_num = len(input_dict)
        min_list = []
        max_num = 0
        max_list = []
        for temp_char in temp_str:
            if output_dict[temp_char] < min_num:
                min_num = output_dict[temp_char]
                min_list = [temp_char]
            elif output_dict[temp_char] == min_num and temp_char not in min_list:
                min_list.append(temp_char)

            if output_dict[temp_char] > max_num:
                max_num = output_dict[temp_char]
                max_list = [temp_char]
            elif output_dict[temp_char] == max_num and temp_char not in max_list:
                max_list.append(temp_char)

        min_list.sort()
        max_list.sort()
        min_str = ""
        max_str = ""
        for temp_char in min_list:
            min_str += temp_char
        for temp_char in max_list:
            max_str += temp_char

        print("{0} {1} {2} {3}".format(min_str, min_num, max_str, max_num))

        temp_str = sys.stdin.readline().rstrip()
    return


if __name__ == '__main__':
    main()
