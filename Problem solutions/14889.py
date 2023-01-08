import sys, math


"""
Desc: Calculates difference of ability points between two teams

Parameters
people_num: Number of total people that is divided between teams
check_list: Contains a list of integers for a single team
input_arr: Contains an array of integers with ability points between people
"""


def check_points(people_num: int, check_list: list, input_arr: list) -> int:
    # Make a list of integers for the other team
    other_list = [temp_index for temp_index in range(people_num) if temp_index not in check_list]
    # Number that is returned as output
    output_num = 0
    # Iterate through the whole list
    for first_index in range(people_num // 2 - 1):
        for second_index in range(first_index + 1, people_num // 2):
            # Calculate an iteration for the inputted team
            first_point = input_arr[check_list[first_index]][check_list[second_index]]
            first_point += input_arr[check_list[second_index]][check_list[first_index]]
            # Calculate an iteration for the other team
            second_point = input_arr[other_list[first_index]][other_list[second_index]]
            second_point += input_arr[other_list[second_index]][other_list[first_index]]
            # Get the difference between iteration points
            output_num += first_point - second_point
    # Return the difference between both teams
    return abs(output_num)


"""
Desc: Divides teams for a certain number of people then calls check_points function.
      Minimal output is saved and returned.

Parameters
people_num: Number of total people that is divided between teams
next_int: Starts next iteration from this number
check_list: Contains a list of integers for a single team
input_arr: Contains an array of integers with ability points between people
"""


def repeat_arr(people_num: int, next_int: int, check_list: list, input_arr: list) -> int:
    # If the team is divided already
    if len(check_list) == people_num // 2:
        # Call function to calculate ability difference between two teams
        return check_points(people_num, check_list, input_arr)
    # Save minimum output as variable
    min_output = math.inf
    # Iterate through the list starting at next_int
    for temp_num in range(next_int, people_num - people_num // 2 + len(check_list) + 1):
        # Update team list
        check_list.append(temp_num)
        # Iterate till team is divided
        min_output = min(repeat_arr(people_num, temp_num + 1, check_list, input_arr), min_output)
        # Pop last teammate
        check_list.pop()
    # Return smallest difference
    return min_output


people_num = int(sys.stdin.readline().rstrip())
input_arr = [list(map(int, sys.stdin.readline().rstrip().split(sep=' '))) for _ in range(people_num)]


print(repeat_arr(people_num, 0, [], input_arr))