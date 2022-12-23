import sys


input = sys.stdin.readline


def dfs(r, c, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1:
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr))

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)














import sys
from collections import deque


D_HEIGHT = [1, -1, 0, 0]
D_WIDTH = [0, 0, 1, -1]


# do dfs to input_map and add 1 when encountering a letter that is not X
# if a letter that is not X is encountered then erase using dfs
# if the change the color to lower case if the color blind person saw it
def bfs(input_map, input_len, temp_height, temp_width, is_cap):
    start_char = input_map[temp_height][temp_width]
    is_r_g = ~(input_map[temp_height][temp_width] == "B")
    input_map[temp_height][temp_width] = "X"
    temp_queue = deque([[temp_height, temp_width]])
    while temp_queue:
        temp_height, temp_width = temp_queue.popleft()
        for d_height, d_width in zip(D_HEIGHT, D_WIDTH):
            check_height = temp_height + d_height
            check_width = temp_width + d_width
            if 0 <= check_height < input_len and 0 <= check_width < input_len:
                if input_map[check_height][check_width] == 'X':
                    continue
                if is_r_g:
                    if input_map[check_height][check_width] == 'B':
                        continue
                    if is_cap:
                        if input_map[check_height][check_width] == 'R':
                            input_map[check_height][check_width] = 'r'
                            temp_queue.append([check_height, check_width])
                        if input_map[check_height][check_width] == 'G':
                            input_map[check_height][check_width] = 'g'
                            temp_queue.append([check_height, check_width])
                    else:
                        if input_map[check_height][check_width] == start_char:
                            input_map[check_height][check_width] = "X"
                            temp_queue.append([check_height, check_width])
                else:
                    if input_map[check_height][check_width] != 'B':
                        continue
                    input_map[check_height][check_width] = 'X'
                    temp_queue.append([check_height, check_width])


def color_map(input_map, input_len):
    output_arr = [0, 0]
    for temp_height in range(input_len):
        for temp_width in range(input_len):
            if input_map[temp_height][temp_width] == 'X':
                continue
            if input_map[temp_height][temp_width] in ["R", "G", "B"]:
                if input_map[temp_height][temp_width] == "B":
                    output_arr[0] += 1
                output_arr[1] += 1
                bfs(input_map, input_len, temp_height, temp_width, True)
            bfs(input_map, input_len, temp_height, temp_width, False)
            output_arr[1] += 1
    return output_arr


input_len = int(sys.stdin.readline().rstrip())
input_arr = []
for _ in range(input_len):
    input_arr.append(list(sys.stdin.readline().rstrip()))
output_arr = color_map(input_arr, input_len)
print(output_arr)
