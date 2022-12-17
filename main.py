import sys


class MinHeap:
    def __init__(self):
        self.arr = []
        self.arr_len = 0

    def empty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False

    def insert(self, num):
        index = len(self.arr)
        self.arr.append(num)
        while index != 0:
            next_index = (index - 1) // 2
            if self.arr[next_index] < self.arr[index]:
                break
            self.arr[next_index], self.arr[index] = self.arr[index], self.arr[next_index]
            index = next_index
        self.arr_len += 1

    def pop(self):
        if self.empty():
            return 0
        output_num = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        index = 0
        while True:
            next_index = 2 * index + 1
            min_index = index
            min_val = self.arr[index]
            if next_index < len(self.arr) and self.arr[next_index] < self.arr[index]:

            next_index += 1
            if next_index < len(self.arr):


        return output_num


instruct_num = int(sys.stdin.readline().rstrip())
min_heap = MinHeap()
for _ in range(instruct_num):
    input_num = int(sys.stdin.readline().rstrip())
    if input_num == 0:
        print(min_heap.pop())
    else:
        min_heap.insert(input_num)
