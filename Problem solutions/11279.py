import sys


class MaxHeap:
    def __init__(self, max_range):
        self.arr = [0 for _ in range(max_range)]
        self.size = 0

    def empty(self):
        if self.size == 0:
            return True
        return False

    def insert(self, input_num):
        self.size += 1
        self.arr[self.size] = input_num
        temp_index = self.size
        while temp_index > 1:
            if self.arr[temp_index] <= self.arr[temp_index // 2]:
                break
            self.arr[temp_index], self.arr[temp_index // 2] = self.arr[temp_index // 2], self.arr[temp_index]
            temp_index //= 2

    def pop(self):
        if self.empty():
            return 0
        self.arr[self.size], self.arr[1] = self.arr[1], self.arr[self.size]
        temp_index = 1
        while 2 * temp_index < self.size:
            comp_index = 2 * temp_index
            if comp_index + 1 < self.size and self.arr[comp_index] < self.arr[comp_index + 1]:
                comp_index += 1
            if self.arr[comp_index] < self.arr[temp_index]:
                break
            self.arr[comp_index], self.arr[temp_index] = self.arr[temp_index], self.arr[comp_index]
            temp_index = comp_index
        self.size -= 1
        return self.arr[self.size + 1]


instruct_num = int(sys.stdin.readline().rstrip())
max_heap = MaxHeap(instruct_num)
for _ in range(instruct_num):
    input_num = int(sys.stdin.readline().rstrip())
    if input_num == 0:
        print(max_heap.pop())
    else:
        max_heap.insert(input_num)

