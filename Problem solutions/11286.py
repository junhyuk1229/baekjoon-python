import sys


class AbsMinHeap:
    def __init__(self, max_size):
        self.input_arr = [0] * max_size
        self.arr_size = 0
        self.MAX_SIZE = max_size

    def left_child(self, index):
        return self.input_arr[index * 2]

    def right_child(self, index):
        return self.input_arr[index * 2 + 1]

    def parent(self, index):
        return self.input_arr[index // 2]

    def swap(self, first_index, second_index):
        temp_num = self.input_arr[first_index]
        self.input_arr[first_index] = self.input_arr[second_index]
        self.input_arr[second_index] = temp_num

    def empty(self):
        if self.arr_size == 0:
            return True
        return False

    def insert(self, input_num):
        self.arr_size += 1
        self.input_arr[self.arr_size] = input_num
        self.heap_up(self.arr_size)

    def heap_up(self, index_num):
        while index_num > 1:
            if abs(self.input_arr[index_num]) > abs(self.parent(index_num)):
                break
            if abs(self.input_arr[index_num]) == abs(self.parent(index_num)):
                if self.input_arr[index_num] >= self.parent(index_num):
                    break
            self.swap(index_num, index_num // 2)
            index_num //= 2

    def delete(self):
        if self.empty():
            return 0
        self.swap(1, self.arr_size)
        self.arr_size -= 1
        self.heap_down(1)
        return self.input_arr[self.arr_size + 1]

    def heap_down(self, index_num):
        while index_num * 2 <= self.arr_size:
            comp_index = index_num * 2
            if comp_index + 1 <= self.arr_size:
                if abs(self.left_child(index_num)) > abs(self.right_child(index_num)) or (abs(self.left_child(index_num)) == abs(self.right_child(index_num)) and self.left_child(index_num) > self.right_child(index_num)):
                    comp_index += 1
            if abs(self.input_arr[index_num]) < abs(self.input_arr[comp_index]) or (abs(self.input_arr[index_num]) == abs(self.input_arr[comp_index]) and self.input_arr[index_num] < self.input_arr[comp_index]):
                break
            self.swap(index_num, comp_index)
            index_num = comp_index


instruct_num = int(sys.stdin.readline().rstrip())
temp_heap = AbsMinHeap(instruct_num)
for _ in range(instruct_num):
    temp_num = int(sys.stdin.readline().rstrip())
    if temp_num == 0:
        print(temp_heap.delete())
    else:
        temp_heap.insert(temp_num)
