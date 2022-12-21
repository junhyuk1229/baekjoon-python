import sys

def floyd(dist):
    for r in range(len(dist)):
        for p in range(len(dist)):
            for q in range(len(dist)):
                if dist[p][r] == 1 and dist[r][q]:
                    dist[p][q] = 1


input_num = int(sys.stdin.readline().rstrip())
input_arr = []
for _ in range(input_num):
    input_arr.append(list(map(int, sys.stdin.readline().rstrip().split(sep=' '))))
floyd(input_arr)
for temp_arr in input_arr:
    print(' '.join(map(str, temp_arr)))
