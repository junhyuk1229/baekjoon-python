import sys


# List to save fibo lists
g_fibo_list = [0, 1]


def get_fibo_num(input_num) -> int:
    """
        Get fibonacci number from global list if possible, else calculate till the index wanted
        Arguments:
            input_num: the index of fibonacci list wanted
        Returns:
            The fibonacci number for the index inputted
    """

    # While the fibonacci list doesn't have the index
    while input_num >= len(g_fibo_list):
        # Add another list to the end of the global list using the last two lists
        g_fibo_list.append(g_fibo_list[-1] + g_fibo_list[-2])

        # Log change
        print(f"{g_fibo_list[-1]} added to list")

    # Return the fibonacci list from the global list
    return g_fibo_list[input_num]


def main() -> None:
    # Number of test cases
    case_num = int(sys.stdin.readline().rstrip())

    # Loop for each test case
    for _ in range(case_num):
        # Get input number
        input_num = int(sys.stdin.readline().rstrip())

        # Check input_num
        print(f"input_num: {input_num}")

        # Check list for input num as index
        output_list = [get_fibo_num(input_num - 1), get_fibo_num(input_num)]

        # Check exception
        if input_num == 0:
            output_list = [1, 0]

        # Check output_list
        print(f"output_num: {output_list}")

        # Print output list
        print(' '.join(map(str, output_list)))

    return


if __name__ == '__main__':
    main()