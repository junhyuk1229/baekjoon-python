import sys
import math


class MaxMinHeap:
    def __init__(self, max_len):
        self.heap_arr = [0 for _ in range(max_len + 1)]
        self.arr_len = 0

    def empty(self):
        if self.arr_len == 0:
            return True
        return False

    def is_min_level(self):
        if math.floor(math.log2(self.arr_len)) % 2 == 1:
            return False
        return True

    def insert_num(self, input_num):
        self.arr_len += 1
        self.heap_arr[self.arr_len] = input_num
        if self.arr_len == 1:
            return
        elif self.is_min_level():
            self.min_insert()
        else:
            self.max_insert()

    def max_insert(self):
        if self.heap_arr[self.arr_len // 2] > self.heap_arr[self.arr_len]:
            self.heap_arr[self.arr_len], self.heap_arr[self.arr_len // 2] = self.heap_arr[self.arr_len // 2], self.heap_arr[self.arr_len]
            self.minify_up(self.arr_len // 2)
        else:
            self.maxity_up(self.arr_len)

    def min_insert(self):
        if self.heap_arr[self.arr_len // 2] < self.heap_arr[self.arr_len]:
            self.heap_arr[self.arr_len], self.heap_arr[self.arr_len // 2] = self.heap_arr[self.arr_len // 2], self.heap_arr[self.arr_len]
            self.maxity_up(self.arr_len // 2)
        else:
            self.minify_up(self.arr_len)

    def max_output(self):
        if self.empty():
            return -1
        if self.arr_len == 1:
            self.arr_len -= 1
            return self.heap_arr[1]
        temp_index = 2
        if temp_index + 1 <= self.arr_len and self.heap_arr[temp_index] < self.heap_arr[temp_index + 1]:
            temp_index += 1
        self.heap_arr[self.arr_len], self.heap_arr[temp_index] = self.heap_arr[temp_index], self.heap_arr[self.arr_len]
        self.arr_len -= 1
        self.maxify_down(temp_index)
        return self.heap_arr[self.arr_len + 1]

    def min_output(self):
        if self.empty():
            return -1
        self.heap_arr[self.arr_len], self.heap_arr[1] = self.heap_arr[1], self.heap_arr[self.arr_len]
        self.arr_len -= 1
        self.minify_down(1)
        return self.heap_arr[self.arr_len + 1]

    def maxify_down(self, input_index):
        while input_index * 2 <= self.arr_len:
            if input_index * 4 > self.arr_len:
                comp_index = input_index * 2
                if comp_index + 1 == self.arr_len and self.heap_arr[comp_index] < self.heap_arr[comp_index]:
                    comp_index += 1
                if self.heap_arr[input_index] < self.heap_arr[comp_index]:
                    self.heap_arr[input_index], self.heap_arr[comp_index] = self.heap_arr[comp_index], self.heap_arr[input_index]
                return
            comp_index = input_index * 2 + 1
            for temp_index in range(input_index * 4, input_index * 4 + 4):
                if temp_index + 1 == self.arr_len and self.heap_arr[comp_index] < self.heap_arr[temp_index]:
                    comp_index = temp_index
            self.heap_arr[input_index], self.heap_arr[comp_index] = self.heap_arr[comp_index], self.heap_arr[input_index]
            if comp_index == input_index * 2 + 1:
                return
            if self.heap_arr[comp_index] < self.heap_arr[comp_index // 2]:
                self.heap_arr[comp_index // 2], self.heap_arr[comp_index] = self.heap_arr[comp_index], self.heap_arr[comp_index // 2]
            input_index = comp_index

    def minify_down(self, input_index):
        while input_index * 2 <= self.arr_len:
            if input_index * 4 > self.arr_len:
                comp_index = input_index * 2
                if comp_index + 1 == self.arr_len and self.heap_arr[comp_index] > self.heap_arr[comp_index]:
                    comp_index += 1
                if self.heap_arr[input_index] > self.heap_arr[comp_index]:
                    self.heap_arr[input_index], self.heap_arr[comp_index] = self.heap_arr[comp_index], self.heap_arr[input_index]
                return
            comp_index = input_index * 2 + 1
            for temp_index in range(input_index * 4, input_index * 4 + 4):
                if temp_index + 1 == self.arr_len and self.heap_arr[comp_index] > self.heap_arr[temp_index]:
                    comp_index = temp_index
            self.heap_arr[input_index], self.heap_arr[comp_index] = self.heap_arr[comp_index], self.heap_arr[input_index]
            if comp_index == input_index * 2 + 1:
                return
            if self.heap_arr[comp_index] > self.heap_arr[comp_index // 2]:
                self.heap_arr[comp_index // 2], self.heap_arr[comp_index] = self.heap_arr[comp_index], self.heap_arr[comp_index // 2]
            input_index = comp_index

    def maxity_up(self, input_index):
        while input_index // 4 > 0:
            comp_index = input_index // 4
            if self.heap_arr[comp_index] >= self.heap_arr[input_index]:
                break
            self.heap_arr[comp_index], self.heap_arr[input_index] = self.heap_arr[input_index], self.heap_arr[comp_index]
            input_index = comp_index

    def minify_up(self, input_index):
        while input_index // 4 > 0:
            comp_index = input_index // 4
            if self.heap_arr[comp_index] <= self.heap_arr[input_index]:
                break
            self.heap_arr[comp_index], self.heap_arr[input_index] = self.heap_arr[input_index], self.heap_arr[comp_index]
            input_index = comp_index


case_num = int(sys.stdin.readline().rstrip())
for _ in range(case_num):
    instruct_num = int(sys.stdin.readline().rstrip())
    max_min_heap = MaxMinHeap(instruct_num)
    for _ in range(instruct_num):
        input_type, input_num = sys.stdin.readline().rstrip().split(sep=' ')
        if input_type == 'I':
            max_min_heap.insert_num(int(input_num))
            continue
        if input_num == '1':
            max_min_heap.max_output()
        else:
            max_min_heap.min_output()
    max_num = max_min_heap.max_output()
    min_num = max_min_heap.min_output()
    if max_num == -1:
        print("EMPTY")
    elif min_num == -1:
        print(f"{max_num} {max_num}")
    else:
        print(f"{max_num} {min_num}")
