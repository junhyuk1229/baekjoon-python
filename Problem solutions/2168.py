import sys


def get_gcd(large_num: int, small_num: int) -> int:
    # If the answer is created
    if small_num == 0:
        return large_num

    # Get next iteration
    large_num, small_num = small_num, large_num % small_num
    return get_gcd(large_num, small_num)


def main() -> None:
    # Get input
    first_num, second_num = map(int, sys.stdin.readline().rstrip().split(sep=' '))

    # Get large/small number
    if first_num > second_num:
        large_num, small_num = first_num, second_num
    else:
        large_num, small_num = second_num, first_num

    # Find common denominator
    gcd = get_gcd(large_num, small_num)
    large_num //= gcd
    small_num //= gcd

    output_num = (large_num + small_num - 1) * gcd

    # Print output
    print(output_num)


if __name__ == '__main__':
    main()
