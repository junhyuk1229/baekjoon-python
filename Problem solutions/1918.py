import sys
from collections import deque


PRIO_DICT = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1
}


input_str = sys.stdin.readline().rstrip()
output_stack = deque()
prio_sym_stack = deque()
prio_num = 0
curr_prio = 0


for temp_char in input_str:
    if temp_char.isalpha():
        output_stack.append(temp_char)
        continue
    if temp_char == '(':
        curr_prio += 2
        continue
    if temp_char == ')':
        curr_prio -= 2
        continue
    temp_prio = PRIO_DICT[temp_char] + curr_prio
    if prio_num == 0 or prio_sym_stack[-1][0] < temp_prio:
        prio_sym_stack.append([temp_prio, temp_char])
        prio_num += 1
        continue
    while prio_num != 0 and prio_sym_stack[-1][0] >= temp_prio:
        second_str = output_stack.pop()
        first_str = output_stack.pop()
        temp_sym = prio_sym_stack.pop()[1]
        output_stack.append(first_str + second_str + temp_sym)
        prio_num -= 1
    prio_sym_stack.append([temp_prio, temp_char])
    prio_num += 1


while prio_sym_stack:
    second_str = output_stack.pop()
    first_str = output_stack.pop()
    temp_sym = prio_sym_stack.pop()[1]
    output_stack.append(first_str + second_str + temp_sym)


print(output_stack.pop())
