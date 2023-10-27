from collections import deque
import sys


def main() -> None:
    gear_list = [deque(sys.stdin.readline().rstrip()) for _ in range(4)]

    turn_num = int(sys.stdin.readline().rstrip())

    for _ in range(turn_num):
        gear_num, turn_dir = map(int, sys.stdin.readline().rstrip().split(sep=' '))

        turn_list = [0] * 4
        turn_list[gear_num - 1] = turn_dir

        # Check Forwards
        for temp_gear_num in range(gear_num - 1, 3):
            if gear_list[temp_gear_num][2] == gear_list[temp_gear_num + 1][6]:
                break

            turn_list[temp_gear_num + 1] = turn_list[temp_gear_num] * -1

        # Check Backwards
        for temp_gear_num in range(gear_num - 1, 0, -1):
            if gear_list[temp_gear_num][6] == gear_list[temp_gear_num - 1][2]:
                break

            turn_list[temp_gear_num - 1] = turn_list[temp_gear_num] * -1

        # Turn Gears
        for gear_num, turn_dir in enumerate(turn_list):
            if turn_dir == 1:
                gear_list[gear_num].appendleft(gear_list[gear_num].pop())
            elif turn_dir == -1:
                gear_list[gear_num].append(gear_list[gear_num].popleft())

    # Calculate Score
    output_num = 0

    for score_num, temp_gear in zip([1, 2, 4, 8], gear_list):
        if temp_gear[0] == '1':
            output_num += score_num

    print(output_num)

    return


if __name__ == '__main__':
    main()
