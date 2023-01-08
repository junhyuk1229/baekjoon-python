from collections import deque


class Stack:
    def __init__(self):
        # Stack for saving values
        self.stack = deque()
        # Length of the stack
        self.length = 0

    """Returns length of stack"""
    def __len__(self):
        return self.length

    """Checks if stack is empty"""
    def empty(self):
        if self.length == 0:
            return True
        return False

    """Pushes arguments to stack"""
    def stack_push(self, *args):
        for value in args:
            self.length += 1
            self.stack.append(value)

    """Pops arguments as output"""
    def stack_pop(self, pop_num=1, error_num=-1):
        # Check if pop number is greater than 0
        if pop_num <= 0:
            raise ValueError("Can't pop negative or zero values")
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
