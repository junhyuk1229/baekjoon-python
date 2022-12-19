import sys
import math


class MaxMinHeap:
    def __init__(self, max_len):
        self.heap_arr = [0 for _ in range(max_len + 1)]
        self.arr_len = 0

    # checks if heap is empty
    def empty(self):
        if self.arr_len == 0:
            return True
        return False

    # checks if the level of the tree is an odd number or an even number
    def is_min_level(self):
        if math.floor(math.log2(self.arr_len)) % 2 == 1:
            return False
        return True

    # inserts a number to the heap
    def insert_num(self, input_num):
        self.arr_len += 1
        self.heap_arr[self.arr_len] = input_num
        # if the array was empty, don't do any checks
        if self.arr_len == 1:
            return
        # else if the array is at the min level of the tree
        elif self.is_min_level():
            self.min_insert()
        else:
            self.max_insert()

    # when a number is added to the heap at the max level
    def max_insert(self):
        # if the child is bigger than the number
        if self.heap_arr[self.arr_len // 2] > self.heap_arr[self.arr_len]:
            # change the values
            self.heap_arr[self.arr_len], self.heap_arr[self.arr_len // 2] = self.heap_arr[self.arr_len // 2], self.heap_arr[self.arr_len]
            # keep updating the values up the min tree
            self.minify_up(self.arr_len // 2)
        else:
            # keep updating the values up the max tree
            self.maxity_up(self.arr_len)

    # when a number is added to the heap at the min level
    def min_insert(self):
        # if the child is smaller than the number
        if self.heap_arr[self.arr_len // 2] < self.heap_arr[self.arr_len]:
            # change the values
            self.heap_arr[self.arr_len], self.heap_arr[self.arr_len // 2] = self.heap_arr[self.arr_len // 2], self.heap_arr[self.arr_len]
            # keep updating the values up the max tree
            self.maxity_up(self.arr_len // 2)
        else:
            # keep updating the values up the min tree
            self.minify_up(self.arr_len)

    # when a max number is needed
    def max_output(self):
        if self.empty():
            return -1
        # if there is only one number(the first node is in the min level) return that node
        if self.arr_len == 1:
            self.arr_len -= 1
            return self.heap_arr[1]
        # else check the second and third node to get max num
        temp_index = 2
        if temp_index + 1 <= self.arr_len and self.heap_arr[temp_index] < self.heap_arr[temp_index + 1]:
            temp_index += 1
        # change with the last element
        self.heap_arr[self.arr_len], self.heap_arr[temp_index] = self.heap_arr[temp_index], self.heap_arr[self.arr_len]
        self.arr_len -= 1
        # go updating down the array
        self.maxify_down(temp_index)
        # print the max that was changed with the last element
        return self.heap_arr[self.arr_len + 1]

    # when a min number is needed
    def min_output(self):
        if self.empty():
            return -1
        # change with the last element(the min number is always at index 1)
        self.heap_arr[self.arr_len], self.heap_arr[1] = self.heap_arr[1], self.heap_arr[self.arr_len]
        self.arr_len -= 1
        # go updating down the array
        self.minify_down(1)
        # print the min that was changed with the last element
        return self.heap_arr[self.arr_len + 1]

    # when an output is sent from the max level
    def maxify_down(self, input_index):
        # while the node has a child
        while input_index * 2 <= self.arr_len:
            # if there are no grandchild
            if input_index * 4 > self.arr_len:
                # check the child
                comp_index = input_index * 2
                if comp_index + 1 == self.arr_len and self.heap_arr[comp_index] < self.heap_arr[comp_index]:
                    comp_index += 1
                # if any of the child are bigger change values
                if self.heap_arr[input_index] < self.heap_arr[comp_index]:
                    self.heap_arr[input_index], self.heap_arr[comp_index] = self.heap_arr[comp_index], self.heap_arr[input_index]
                # end update
                return
            # else set the comparing element to its right child
            # this is because the right child might have no child. Making this node have no guarantee that it is
            # smaller than the grandchild
            comp_index = input_index * 2 + 1
            # loop through the grandchild list
            for temp_index in range(input_index * 4, input_index * 4 + 4):
                if temp_index + 1 == self.arr_len and self.heap_arr[comp_index] < self.heap_arr[temp_index]:
                    comp_index = temp_index
            # swap the max number with the index
            self.heap_arr[input_index], self.heap_arr[comp_index] = self.heap_arr[comp_index], self.heap_arr[input_index]
            # if the swaped index was the child one end update
            if comp_index == input_index * 2 + 1:
                return
            # else check the parent of the node for any errors
            if self.heap_arr[comp_index] < self.heap_arr[comp_index // 2]:
                self.heap_arr[comp_index // 2], self.heap_arr[comp_index] = self.heap_arr[comp_index], self.heap_arr[comp_index // 2]
            # set the index again and loop
            input_index = comp_index

    # when an output is sent from the max level
    def minify_down(self, input_index):
        # while the node has a child
        while input_index * 2 <= self.arr_len:
            # if there are no grandchild
            if input_index * 4 > self.arr_len:
                # check the child
                comp_index = input_index * 2
                if comp_index + 1 == self.arr_len and self.heap_arr[comp_index] > self.heap_arr[comp_index]:
                    comp_index += 1
                # if any of the parents are bigger change values
                if self.heap_arr[input_index] > self.heap_arr[comp_index]:
                    self.heap_arr[input_index], self.heap_arr[comp_index] = self.heap_arr[comp_index], self.heap_arr[input_index]
                # end update
                return
            # else set the comparing element to its right child
            # this is because the right child might have no child. Making this node have no guarantee that it is
            # bigger than the grandchild
            comp_index = input_index * 2 + 1
            # loop through the grandchild list
            for temp_index in range(input_index * 4, input_index * 4 + 4):
                if temp_index + 1 == self.arr_len and self.heap_arr[comp_index] > self.heap_arr[temp_index]:
                    comp_index = temp_index
            # swap the min number with the index
            self.heap_arr[input_index], self.heap_arr[comp_index] = self.heap_arr[comp_index], self.heap_arr[input_index]
            # if the swaped index was the child one end update
            if comp_index == input_index * 2 + 1:
                return
            # else check the parent of the node for any errors
            if self.heap_arr[comp_index] > self.heap_arr[comp_index // 2]:
                self.heap_arr[comp_index // 2], self.heap_arr[comp_index] = self.heap_arr[comp_index], self.heap_arr[comp_index // 2]
            # set the index again and loop
            input_index = comp_index

    # when input is in max level
    def maxity_up(self, input_index):
        # while the input has a grandfather
        while input_index // 4 > 0:
            # compare grandfather with input and if input is greater swap
            comp_index = input_index // 4
            if self.heap_arr[comp_index] >= self.heap_arr[input_index]:
                break
            self.heap_arr[comp_index], self.heap_arr[input_index] = self.heap_arr[input_index], self.heap_arr[comp_index]
            # update index and loop
            input_index = comp_index

    # when input is in min level
    def minify_up(self, input_index):
        # while the input has a grandfather
        while input_index // 4 > 0:
            # compare grandfather with input and if input is smaller swap
            comp_index = input_index // 4
            if self.heap_arr[comp_index] <= self.heap_arr[input_index]:
                break
            self.heap_arr[comp_index], self.heap_arr[input_index] = self.heap_arr[input_index], self.heap_arr[comp_index]
            # update index and loop
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
