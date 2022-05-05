import sys

a = input()                                 # gets a input till we get a new line
b = int(input())                            # used in 1 input for int
c1, c2 = map(int, input().split(sep=' '))   # splits the input with sep and changes to int
d = list(map(int, input().split(sep=' ')))  # saves a list
e = sys.stdin.readline().rstrip()           # used to read line with less time + rstrip() is used to delete the \n char
f = list(map(int, sys.stdin.readline().split(sep=' ')))