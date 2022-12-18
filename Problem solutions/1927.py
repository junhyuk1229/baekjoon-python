import sys


class MinHeap:
    def __init__(self, max_size):
        self.arr = [0 for _ in range(max_size + 1)]
        self.arr_len = 0

    def empty(self):
        if self.arr_len == 0:
            return True
        else:
            return False

    def insert(self, num):
        self.arr_len += 1
        self.arr[self.arr_len] = num
        temp_index = self.arr_len
        while temp_index != 1:
            if self.arr[temp_index] >= self.arr[temp_index // 2]:
                break
            self.arr[temp_index], self.arr[temp_index // 2] = self.arr[temp_index // 2], self.arr[temp_index]
            temp_index //= 2

    def pop(self):
        if self.empty():
            return 0
        self.arr[1], self.arr[self.arr_len] = self.arr[self.arr_len], self.arr[1]
        self.arr_len -= 1
        temp_index = 1
        while temp_index * 2 <= self.arr_len:
            comp_index = temp_index * 2
            if comp_index != self.arr_len and self.arr[comp_index] > self.arr[comp_index + 1]:
                comp_index += 1
            if self.arr[comp_index] >= self.arr[temp_index]:
                break
            self.arr[comp_index], self.arr[temp_index] = self.arr[temp_index], self.arr[comp_index]
            temp_index = comp_index
        return self.arr[self.arr_len + 1]


instruct_num = int(sys.stdin.readline().rstrip())
min_heap = MinHeap(instruct_num)
for _ in range(instruct_num):
    input_num = int(sys.stdin.readline().rstrip())
    if input_num == 0:
        print(min_heap.pop())
    else:
        min_heap.insert(input_num)
