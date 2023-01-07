import sys


input_str = sys.stdin.readline().rstrip('\n')
for temp_char in input_str:
    if temp_char.isalpha():
        changed_ascii = ord(temp_char) + 13
        compare_ascii = ord('z')
        if temp_char.isupper():
            compare_ascii = ord('Z')
        if changed_ascii > compare_ascii:
            changed_ascii -= 26
        print(chr(changed_ascii), end='')
    else:
        print(temp_char, end='')
