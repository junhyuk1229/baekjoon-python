import sys


def main():
    dic_num, quest_num = map(int, sys.stdin.readline().split(sep=' '))
    dic_list = [0] * dic_num
    dic_dic = {}
    for i in range(dic_num):
        dic_list[i] = sys.stdin.readline().rstrip()
    for i in range(dic_num):
        dic_dic[dic_list[i]] = i
    for _ in range(quest_num):
        temp_input = sys.stdin.readline().rstrip()
        if '0' <= temp_input[0] <= '9':
            print(dic_list[int(temp_input) - 1])
        else:
            print(dic_dic[temp_input] + 1)
        


if __name__ == "__main__":
    main()
