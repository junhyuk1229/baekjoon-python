import sys, math, random


class MaxMinHeap:
    def __init__(self, max_len):
        # Has the actual heap
        self.heap_arr = [0 for _ in range(max_len + 1)]
        # The array length
        self.arr_len = 0

    # checks if the array is empty
    def empty(self):
        if self.arr_len == 0:
            return True
        return False

    # checks if the level of the input is min
    def is_min_level(self):
        if math.floor(math.log2(self.arr_len)) % 2 == 1:
            return False
        return True

    # inputs a number to the min-max heap
    def insert_num(self, input_num):
        # add 1 to the length of the heap
        self.arr_len += 1
        # set the number to the last index of the array
        self.heap_arr[self.arr_len] = input_num
        # if the input is at the root
        if self.arr_len == 1:
            return
        # if the input is at the min level
        elif self.is_min_level():
            self.min_insert()
        # if the input is at the max level
        else:
            self.max_insert()

    def max_insert(self):
        # if the number is inserted at the max level check if the parent is bigger
        if self.heap_arr[self.arr_len // 2] > self.heap_arr[self.arr_len]:
            # switch the numbers parent and child
            self.heap_arr[self.arr_len], self.heap_arr[self.arr_len // 2] = self.heap_arr[self.arr_len // 2], self.heap_arr[self.arr_len]
            # update the min level from the parent position
            self.minify_up(self.arr_len // 2)
        # if the parent is smaller
        else:
            # update the max level from the current position
            self.maxity_up(self.arr_len)

    def min_insert(self):
        # if the number is inserted at the max level check if the parent is bigger
        if self.heap_arr[self.arr_len // 2] < self.heap_arr[self.arr_len]:
            # switch the numbers parent and child
            self.heap_arr[self.arr_len], self.heap_arr[self.arr_len // 2] = self.heap_arr[self.arr_len // 2], self.heap_arr[self.arr_len]
            # update the min level from the parent position
            self.maxity_up(self.arr_len // 2)
        # if the parent is smaller
        else:
            # update the max level from the current position
            self.minify_up(self.arr_len)

    def max_output(self):
        # if the array is empty return 'None'
        if self.empty():
            return None
        # if the array has only 1 value remove root and return the value
        if self.arr_len == 1:
            self.arr_len -= 1
            return self.heap_arr[1]
        # set the output as the left child of root
        temp_index = 2
        # if the right child does exist and the right child is bigger than the left child
        if temp_index + 1 <= self.arr_len and self.heap_arr[temp_index] < self.heap_arr[temp_index + 1]:
            # change the output as the right child of the root
            temp_index += 1
        # swap the max num with the last index value
        self.heap_arr[self.arr_len], self.heap_arr[temp_index] = self.heap_arr[temp_index], self.heap_arr[self.arr_len]
        # remove the last node from the heap
        self.arr_len -= 1
        # update down the tree from the max node
        self.maxify_down(temp_index)
        # return the deleted node from the heap
        return self.heap_arr[self.arr_len + 1]

    def min_output(self):
        # if the array is empty return 'None'
        if self.empty():
            return None
        # swap the root(min num) to the last index value
        self.heap_arr[self.arr_len], self.heap_arr[1] = self.heap_arr[1], self.heap_arr[self.arr_len]
        # remove the last node from the heap
        self.arr_len -= 1
        # update down the tree from the root
        self.minify_down(1)
        # return the deleted node from the heap
        return self.heap_arr[self.arr_len + 1]

    # update down the heap
    def maxify_down(self, input_index):
        # while the node is not the leaf
        while input_index * 2 <= self.arr_len:
            # if the node has no grandchildren
            if input_index * 4 > self.arr_len:
                # set the compare node to the left child
                comp_index = input_index * 2
                # if there is no right child or the right child is bigger than the left one
                if comp_index + 1 <= self.arr_len and self.heap_arr[comp_index] < self.heap_arr[comp_index + 1]:
                    # change the compare node to the right child
                    comp_index += 1
                # if the compare node has a higher value than the current node
                if self.heap_arr[input_index] < self.heap_arr[comp_index]:
                    # swap the compare node and current node
                    self.heap_arr[input_index], self.heap_arr[comp_index] = self.heap_arr[comp_index], self.heap_arr[input_index]
                # end search because there are no more children for the compare node(from first if statement)
                return
            # else if there are any grandchildren
            # set compare node to the right child(this is set because we know that the left child will be smaller than
            # the grandchildren at the left, but the right node might not have any children)
            comp_index = input_index * 2 + 1
            # loop through the grandchildren
            for temp_index in range(input_index * 4, input_index * 4 + 4):
                # if there is the grandchild and the value is bigger than the value of the compare node
                if temp_index <= self.arr_len and self.heap_arr[comp_index] < self.heap_arr[temp_index]:
                    # change the compare node to the grandchild
                    comp_index = temp_index
            # if the compare node value is bigger than the current node value
            if self.heap_arr[input_index] < self.heap_arr[comp_index]:
                # swap the values
                self.heap_arr[input_index], self.heap_arr[comp_index] = self.heap_arr[comp_index], self.heap_arr[input_index]
            # if the swapped node is the child node
            if comp_index == input_index * 2 + 1:
                # end the value
                return
            # check if the parent node is smaller than the changed node
            if self.heap_arr[comp_index] < self.heap_arr[comp_index // 2]:
                # swap the nodes
                self.heap_arr[comp_index // 2], self.heap_arr[comp_index] = self.heap_arr[comp_index], self.heap_arr[comp_index // 2]
            # change the compare node to the current node
            input_index = comp_index

    # update down the heap
    def minify_down(self, input_index):
        # while the node is not the leaf
        while input_index * 2 <= self.arr_len:
            # if the node has no grandchildren
            if input_index * 4 > self.arr_len:
                # set the compare node to the left child
                comp_index = input_index * 2
                # if there is no right child or the right child is smaller than the left one
                if comp_index + 1 <= self.arr_len and self.heap_arr[comp_index] > self.heap_arr[comp_index + 1]:
                    # change the compare node to the right child
                    comp_index += 1
                # if the compare node has a smaller value than the current node
                if self.heap_arr[input_index] > self.heap_arr[comp_index]:
                    # swap the compare node and current node
                    self.heap_arr[input_index], self.heap_arr[comp_index] = self.heap_arr[comp_index], self.heap_arr[input_index]
                # end search because there are no more children for the compare node(from first if statement)
                return
            # else if there are any grandchildren
            # set compare node to the right child(this is set because we know that the left child will be bigger than
            # the grandchildren at the left, but the right node might not have any children)
            comp_index = input_index * 2 + 1
            # loop through the grandchildren
            for temp_index in range(input_index * 4, input_index * 4 + 4):
                # if there is the grandchild and the value is bigger than the value of the compare node
                if temp_index <= self.arr_len and self.heap_arr[comp_index] > self.heap_arr[temp_index]:
                    # change the compare node to the grandchild
                    comp_index = temp_index
            # if the compare node value is bigger than the current node value
            if self.heap_arr[input_index] > self.heap_arr[comp_index]:
                # swap the values
                self.heap_arr[input_index], self.heap_arr[comp_index] = self.heap_arr[comp_index], self.heap_arr[input_index]
            # check if the parent node is smaller than the changed node
            if comp_index == input_index * 2 + 1:
                # end the value
                return
            # check if the parent node is smaller than the changed node
            if self.heap_arr[comp_index] > self.heap_arr[comp_index // 2]:
                # swap the nodes
                self.heap_arr[comp_index // 2], self.heap_arr[comp_index] = self.heap_arr[comp_index], self.heap_arr[comp_index // 2]
            # change the compare node to the current node
            input_index = comp_index

    # update up the heap
    def maxity_up(self, input_index):
        # while the node has a grandfather
        while input_index // 4 > 0:
            # set the grandfather as the compare index
            comp_index = input_index // 4
            # if the grandfather is bigger than the current node
            if self.heap_arr[comp_index] >= self.heap_arr[input_index]:
                # end update
                break
            # if the current node is bigger swap the values
            self.heap_arr[comp_index], self.heap_arr[input_index] = self.heap_arr[input_index], self.heap_arr[comp_index]
            # update from the grandfather
            input_index = comp_index

    # update up the heap
    def minify_up(self, input_index):
        # set the grandfather as the compare index
        while input_index // 4 > 0:
            # set the grandfather as the compare index
            comp_index = input_index // 4
            # if the grandfather is smaller than the current node
            if self.heap_arr[comp_index] <= self.heap_arr[input_index]:
                # end update
                break
            # if the current node is smaller swap the values
            self.heap_arr[comp_index], self.heap_arr[input_index] = self.heap_arr[input_index], self.heap_arr[comp_index]
            # update from the grandfather
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
    if max_num is None:
        print("EMPTY")
    elif min_num is None:
        print(f"{max_num} {max_num}")
    else:
        print(f"{max_num} {min_num}")
