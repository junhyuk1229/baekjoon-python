import sys


fibo_num = int(sys.stdin.readline().rstrip())
fibo_arr = [0, 1, 1]
for _ in range(fibo_num - 2):
    fibo_arr[0] = fibo_arr[1]
    fibo_arr[1] = fibo_arr[2]
    fibo_arr[2] += fibo_arr[0]
    fibo_num -= 1


print(fibo_arr[fibo_num])
