import sys, math


def sqrd_dist(first_pos, second_pos):
    return (first_pos[0] - second_pos[0]) ** 2.0 + (first_pos[1] - second_pos[1]) ** 2.0


def get_output(tele_data, bug_list):
    for temp_bug in bug_list:
        temp_dist = math.sqrt(sqrd_dist(temp_bug, tele_data[1:]))
        if temp_dist <= tele_data[0] + 1.0:
            return temp_bug
        tele_data[1] += (temp_bug[0] - tele_data[1]) * tele_data[0] / temp_dist
        tele_data[2] += (temp_bug[1] - tele_data[2]) * tele_data[0] / temp_dist
    return


def main():
    tele_data = list(map(float, sys.stdin.readline().rstrip().split(sep=' ')))
    temp_time = 1
    while tele_data[0] != 0:
        bug_list = []
        temp_input = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
        while temp_input != [-1, -1]:
            bug_list.append(temp_input)
            temp_input = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
        output_list = get_output(tele_data, bug_list)
        if output_list is not None:
            print("Firefly {0} caught at ({1},{2})".format(temp_time, output_list[0], output_list[1]))
        else:
            print("Firefly {0} not caught".format(temp_time))
        tele_data = list(map(float, sys.stdin.readline().rstrip().split(sep=' ')))
        temp_time += 1
    return


if __name__ == '__main__':
    main()
