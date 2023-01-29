from collections import deque
import sys


def dfs(people_map, know_list):
    output_list = []
    temp_list = deque()
    temp_map = [False] * len(know_list)
    for temp_index, temp_val in enumerate(know_list):
        if temp_val:
            temp_list.append(temp_index)
            temp_map[temp_index] = True
    print(temp_list)
    print(temp_map)

    while temp_list:
        output_list.append(temp_list.pop())
        for temp_index, temp_val in enumerate(people_map[output_list[-1]]):
            if not temp_val or temp_map[temp_index]:
                continue
            temp_list.append(temp_index)
            temp_map[temp_index] = True
        temp_map[output_list[-1]] = True
    return output_list


def main():
    people_num, party_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    know_list = [False] * people_num
    temp_list = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    for temp_index, temp_num in enumerate(temp_list):
        if temp_index == 0:
            continue
        know_list[temp_num - 1] = True
    print(know_list)

    party_arr = []
    people_map = [[False] * people_num for _ in range(people_num)]
    for _ in range(party_num):
        party_arr.append(list(map(int, sys.stdin.readline().rstrip().split(sep=' '))))
        for first_index in range(1, len(party_arr[-1]) - 1):
            for second_index in range(first_index + 1, len(party_arr[-1])):
                people_map[party_arr[-1][first_index] - 1][party_arr[-1][second_index] - 1] = True
                people_map[party_arr[-1][second_index] - 1][party_arr[-1][first_index] - 1] = True
                print(first_index, second_index)
    for temp_list in people_map:
        print(temp_list)
    print(party_arr)

    output_list = dfs(people_map, know_list)
    print(output_list)

    return


if __name__ == "__main__":
    main()
