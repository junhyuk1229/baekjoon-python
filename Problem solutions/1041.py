import sys

'''
for cube length N where N > 1
1 face = (N - 2) ** 2 * 5 + (N - 2) * 4
2 face = (N - 2) * 8 + 4
3 face = 4

1 face = 5 * (N ** 2) - 16 * N + 12
2 face = 8N - 12
3 face = 4


if N == 1
5 face = 1
'''

# list all possible combinations for 2 face next to each other(edge)
two_face_arr = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 5], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]
# list all possible combinations for 3 face next to each other(point)
three_face_arr = [[0, 1, 2], [0, 1, 3], [0, 2, 4], [0, 3, 4], [1, 2, 5], [1, 3, 5], [2, 4, 5], [3, 4, 5]]

big_cube_size = int(sys.stdin.readline().rstrip())
face_num_arr = list(map(int, sys.stdin.readline().rstrip().split(sep=' ')))
output_num = 0

# only exception is when cube size is 1
if big_cube_size == 1:
    output_num = sum(face_num_arr) - max(face_num_arr)
else:
    # iterate through the list above to get the minimum value for two faces and three faces
    one_face_sum = min(face_num_arr)
    two_face_sum = min(face_num_arr[i] + face_num_arr[j] for i, j in two_face_arr)
    three_face_sum = min(face_num_arr[i] + face_num_arr[j] + face_num_arr[k] for i, j, k in three_face_arr)
    # use calculation above to get answer
    output_num = 4 * three_face_sum + (8 * big_cube_size - 12) * two_face_sum + (5 * big_cube_size ** 2  - 16 * big_cube_size + 12) * one_face_sum

print(output_num)
