from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()
        self.length = 0

    def __len__(self):
        return self.length

    def empty(self):
        if self.length == 0:
            return True
        return False

    def stack_push(self, *args):
        for value in args:
            self.length += 1
            self.stack.append(value)

    def stack_pop(self):
        if self.empty():
            return -1
        self.length -= 1
        return self.stack.pop()

    def stack_peek(self):
        if self.empty():
            return -1
        temp_num = self.stack_pop()
        self.stack_push(temp_num)
        return temp_num

    def clear(self):
        self.stack = deque()
        self.length = 0

    def print(self, sep=" "):
        temp_stack = list(self.stack)
        print(sep.join(map(str, temp_stack)))
