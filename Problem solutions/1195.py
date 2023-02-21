import sys


def main() -> None:
    teeth_list = sys.stdin.readline().rstrip()
    hole_list = sys.stdin.readline().rstrip()

    if len(teeth_list) > len(hole_list):
        teeth_list, hole_list = hole_list, teeth_list

    pad_hole_list = "0" * (len(teeth_list) - 1) + hole_list + "0" * (len(teeth_list) - 1)

    min_len = len(teeth_list) + len(hole_list)

    for temp_dx in range(min_len - 1):
        is_pos = True

        for temp_index, temp_val in enumerate(teeth_list):
            if pad_hole_list[temp_index + temp_dx] != '0' and temp_val == pad_hole_list[temp_index + temp_dx] == '2':
                is_pos = False
                break

        if not is_pos:
            continue

        comp_len = len(hole_list)
        if temp_dx < len(teeth_list) - 1:
            comp_len += len(teeth_list) - temp_dx - 1
        elif temp_dx > len(hole_list) - 1:
            comp_len += temp_dx - len(hole_list) + 1

        min_len = min(min_len, comp_len)

    print(min_len)

    return


if __name__ == '__main__':
    main()
