from collections import deque


class Queue:
    def __init__(self, input_list=None):
        # Queue for saving values
        self.__queue = deque()
        # Length of the queue
        self.length = 0
        if input_list is not None:
            self.queue_push(*input_list)

    """Returns length of queue"""
    def __len__(self):
        return self.length

    """Checks if queue is empty"""
    def empty(self):
        if self.length == 0:
            return True
        return False

    """Pushes arguments to queue"""
    def queue_push(self, *args):
        for value in args:
            self.length += 1
            self.__queue.append(value)

    """Pops arguments as output"""
    def queue_pop(self, pop_num=1, error_num=-1):
        # Check if pop number is greater than 0
        if pop_num <= 0:
            raise ValueError("Can't pop negative or zero values")

        # If many values are returned, return list
        output_arr = deque()
        for _ in range(pop_num):
            if self.empty():
                break
            self.length -= 1
            output_arr.append(self.__queue.popleft())

        if len(output_arr) == 0:
            return error_num
        # If only one value is returned, return value
        if len(output_arr) == 1:
            return output_arr.popleft()
        return list(output_arr)

    """Peeks arguments as output"""
    def queue_peek(self, peek_num=1, error_num=-1):
        # Check if peek number is greater than 0
        if peek_num <= 0:
            raise ValueError("Error can't peek negative or zero vales")
        output_value = self.queue_pop(peek_num, error_num)
        self.queue_push(output_value)
        return output_value

    """Clears queue"""
    def clear(self):
        self.__queue = deque()
        self.length = 0

    """Prints queue"""
    def print(self, empty_message="The Queue is Empty", sep=" "):
        if self.empty():
            print(empty_message)
        else:
            print(sep.join(map(str, list(self.__queue))))
