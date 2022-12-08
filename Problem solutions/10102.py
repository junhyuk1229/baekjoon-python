import sys


def main():
    _ = int(sys.stdin.readline().rstrip())
    input_arr = sys.stdin.readline().rstrip()
    vote_arr = [0, 0]
    for temp_char in input_arr:
        vote_arr[ord(temp_char) - 65] += 1
    if vote_arr[0] < vote_arr[1]:
        print('B')
    elif vote_arr[0] == vote_arr[1]:
        print("Tie")
    else:
        print('A')


if __name__ == "__main__":
    main()
