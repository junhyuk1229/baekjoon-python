from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()
        self.length = 0

    def __len__(self):
        return self.length

    def empty(self):
        if self.length == 0:
            return True
        return False

    def queue_push(self, *args):
        for value in args:
            self.length += 1
            self.queue.append(value)

    def queue_pop(self):
        if self.empty():
            return -1
        self.length -= 1
        return self.queue.popleft()

    def queue_peek(self):
        if self.empty():
            return -1
        temp_num = self.queue_pop()
        self.queue.appendleft(temp_num)
        return temp_num

    def clear(self):
        self.queue = deque()
        self.length = 0

    def print(self, sep=" "):
        temp_queue = list(self.queue)
        print(sep.join(map(str, temp_queue)))
