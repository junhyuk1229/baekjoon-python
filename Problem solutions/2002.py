from collections import deque
import sys


def main() -> None:
    # Get car input number
    car_num = int(sys.stdin.readline().rstrip())
    enter_order = deque()
    exit_order = deque()

    # Get car enter order
    for _ in range(car_num):
        enter_order.append(sys.stdin.readline().rstrip())

    # Checking set
    check_set = set()

    # While the output is not empty
    for _ in range(car_num):
        temp_car = sys.stdin.readline().rstrip()

        if temp_car != enter_order[0]:
            check_set.add(temp_car)
        else:
            enter_order.popleft()

            while enter_order:
                if not enter_order[0] in check_set:
                    break
                else:
                    enter_order.popleft()

    print(len(check_set))


if __name__ == '__main__':
    main()
