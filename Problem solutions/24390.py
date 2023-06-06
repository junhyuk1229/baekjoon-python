from collections import deque
import sys


def bfs(check_list: deque, checked_set: set, input_sec: int) -> deque:
    # Used to save the possible second results
    next_list = deque()

    # Check all possibilities
    while check_list:
        # Get the sec to check
        check_num = check_list.pop()

        # All possible button combinations
        for add_sec in [10, 60, 600]:
            next_num = check_num + add_sec

            # Check if next sec is over the objective or in the visited set
            if next_num > input_sec or next_num in checked_set:
                continue

            # Add result to set and output deque
            checked_set.add(next_num)
            next_list.append(next_num)

    return next_list


def main() -> None:
    # Get input and represent time in seconds
    input_min, input_sec = map(int, sys.stdin.readline().rstrip().split(sep=':'))
    input_sec += input_min * 60

    # With one button press we can think of the following
    #   1. We are at 30 secs and the microwave is running
    #   2. We just turned on the microwave
    level_num = 1
    # Used to check through each layer
    check_list = deque([0, 30])
    # Used to ignore duplicates (saves time for memory)
    checked_set = {0, 30}

    # Go through one iteration of BFS, then check if sec is reached
    while input_sec not in checked_set:
        check_list = bfs(check_list, checked_set, input_sec)
        level_num += 1

    # Print results
    print(level_num)


if __name__ == '__main__':
    main()
