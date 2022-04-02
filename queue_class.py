# Assignment
# Implement the following operations on the Queue class.

# queue.push(item) -> adds an item to the tail of the queue (index 0 of list)
# queue.pop() -> removes and returns an item from the head of the queue (last index of list)
# queue.peek() -> returns an item from the head of the queue
# queue.size() -> returns the number of items in the queue
# Notice that the underlying data type we're using is just a List.

# Hint
# If there are no items in the queue and pop or peek is called, just return None


import random

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        # ?
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        head = self.items[-1]
        del self.items[-1]
        return head


    def peek(self):
        # ?
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        # ?
        return len(self.items)

        # -- TEST SUITE, DON'T TOUCH BELOW THIS LINE --


def main():
    queue = Queue()
    size_queue(queue)
    pop_queue(queue)
    fill_queue(queue, 10)
    peek_queue(queue)
    peek_queue(queue)
    peek_queue(queue)
    peek_queue(queue)
    pop_queue(queue)
    pop_queue(queue)
    pop_queue(queue)
    size_queue(queue)


def size_queue(queue):
    print("size: " + str(queue.size()))
    return queue


def pop_queue(queue):
    print("popping: " + str(queue.pop()))
    print(queue.items)
    return queue


def peek_queue(queue):
    print("peeking: " + str(queue.peek()))
    print(queue.items)
    return queue


def fill_queue(queue, num):
    random.seed(1)
    options = ["banana", "apple", "pear", "carrot", "celery"]
    cars = []
    for i in range(num):
        optionI = random.randint(0, len(options)-1)
        print("pushing: " + options[optionI])
        queue.push(options[optionI])
        print(queue.items)
    return queue


main()