import sys
from collections import deque

# Set movement
d_x = [0, 1, 0, -1]
d_y = [1, 0, -1, 0]


def dfs(input_map: list, start_coor: list, end_coor: list, move_num, output_num: int = 0) -> int:
    # Check if tile is destination
    if start_coor == end_coor:
        if move_num == 0:
            return output_num + 1
        else:
            return output_num

    for temp_x, temp_y in zip(d_x, d_y):
        # Get moved coordinates
        changed_coor = [start_coor[0] + temp_x, start_coor[1] + temp_y]

        # Check out of bounds
        if changed_coor[0] >= len(input_map) or changed_coor[0] < 0:
            continue
        if changed_coor[1] >= len(input_map[0]) or changed_coor[1] < 0:
            continue

        # Check if tile is not visited
        elif not input_map[changed_coor[0]][changed_coor[1]]:
            input_map[changed_coor[0]][changed_coor[1]] = True
            output_num = dfs(input_map, changed_coor, end_coor, move_num - 1, output_num)
            input_map[changed_coor[0]][changed_coor[1]] = False

    return output_num


def main() -> None:
    # Get inputs
    height_num, width_num, dist_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    input_map = list()
    visited_map = list()

    # Get map + visited map
    for h in range(height_num):
        input_map.append(sys.stdin.readline().rstrip())
        visited_map.append([False] * width_num)

        for w in range(width_num):
            if input_map[h][w] == 'T':
                visited_map[h][w] = True

    # Submit 4
    # Set the starting node as visited
    visited_map[height_num - 1][0] = True

    # Submit 3
    # Check for the exception
    # The exception is solved after submission 6
    '''if height_num == width_num == dist_num == 1:
        print(1)
        return'''

    # Submit 6
    # Check if the moves are the type as the distance between both locations(Even/Odd)
    if (height_num + width_num - 1) % 2 != dist_num % 2:
        print(0)
        return

    # Set starting and ending location
    start_h, start_w = height_num - 1, 0
    end_h, end_w = 0, width_num - 1

    case_num = dfs(visited_map, [start_h, start_w], [end_h, end_w], dist_num - 1)

    print(case_num)

    return


if __name__ == '__main__':
    main()
