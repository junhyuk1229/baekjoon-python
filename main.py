import sys


input_list = '>'.join(sys.stdin.readline().rstrip().split(sep='<')).split(sep='>')[0::2]
for temp_str in input_list:
    if temp_str == '':
        continue
    print(temp_str[::-1], end=' ')
