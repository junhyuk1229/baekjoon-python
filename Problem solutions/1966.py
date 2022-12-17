import sys
from collections import deque


case_num = int(sys.stdin.readline().rstrip())
for _ in range(case_num):
    arr_len, search_index = map(int, sys.stdin.readline().rstrip().split(sep=' '))
    prio_index = 0
    print_num = 1
    temp_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
    prio_arr = temp_arr.copy()
    temp_arr = deque(temp_arr)
    prio_arr.sort(reverse=True)
    while True:
        if prio_arr[prio_index] == temp_arr[0]:
            if search_index == 0:
                break
            temp_arr.popleft()
            prio_index += 1
            arr_len -= 1
            print_num += 1
        else:
            if search_index == 0:
                search_index = arr_len
            temp_arr.append(temp_arr.popleft())
        search_index -= 1
    print(print_num)
