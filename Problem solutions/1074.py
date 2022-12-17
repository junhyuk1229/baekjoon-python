import sys


size, row, col = map(int, sys.stdin.readline().rstrip().split(sep=' '))
offset = 0
while size > 0:
    side_num = 0
    if row >= 2 ** (size - 1):
        side_num += 2
        row -= 2 ** (size - 1)
    if col >= 2 ** (size - 1):
        side_num += 1
        col -= 2 ** (size - 1)
    offset += (2 ** size) ** 2 // 4 * side_num
    size -= 1
print(offset)