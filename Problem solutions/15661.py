import sys, math


def recur_score_diff(input_map: list, start_index: int, first_team: list, second_team: list, first_score=0, second_score=0) -> int:
    if start_index == len(input_map):
        if first_score == 0 or second_score == 0:
            return math.inf
        return abs(first_score - second_score)

    # Save total min difference between scores
    min_diff = math.inf

    # Add player to first team
    sum_score = 0
    for temp_val in first_team:
        sum_score += input_map[temp_val][start_index] + input_map[start_index][temp_val]
    first_team.append(start_index)
    comp_diff = recur_score_diff(input_map, start_index + 1, first_team, second_team, first_score + sum_score, second_score)
    min_diff = min(min_diff, comp_diff)
    first_team.pop()

    # Only need to check one side
    # The other is just the same group with the teams flipped
    if start_index == 0:
        return min_diff

    # Add player to second team
    sum_score = 0
    for temp_val in second_team:
        sum_score += input_map[temp_val][start_index] + input_map[start_index][temp_val]
    second_team.append(start_index)
    comp_diff = recur_score_diff(input_map, start_index + 1, first_team, second_team, first_score, second_score + sum_score)
    min_diff = min(min_diff, comp_diff)
    second_team.pop()

    return min_diff


def main() -> None:
    # Get input data
    input_size = int(sys.stdin.readline().rstrip())
    input_map = [list(map(int, sys.stdin.readline().rstrip().split(sep=' '))) for _ in range(input_size)]

    # Print input data
    '''
    print(f"Input size: {input_size}")
    print(f"Input Map:")
    for temp in input_map:
        print(" ".join(map(str, temp)))
    print()
    '''

    # Get output
    print(recur_score_diff(input_map, 0, [], []))

    return


if __name__ == '__main__':
    main()
