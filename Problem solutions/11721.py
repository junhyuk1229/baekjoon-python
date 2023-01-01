import sys, re


split_pattern = '.' * 10
input_str = re.findall('.{1,10}', sys.stdin.readline().rstrip())
print('\n'.join(input_str))
