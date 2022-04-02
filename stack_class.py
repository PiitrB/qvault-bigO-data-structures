# Assignment
# Implement the following methods on the Stack class.

# stack.push(item) -> places a new item on top of the stack
# stack.pop() -> removes the top item from the stack and returns it
# stack.peek() -> returns the top item from the stack without modifying the stack
# stack.size() -> returns the number of items in the stack
# Notice that the underlying data type we're using is just a List, and the methods pop, push, peek, and size aren't necessarily the same for a Python List.

# Hint
# If there are no items in the stack and pop or peek is called, just return None


import random

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item) 

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)

        # -- TEST SUITE, DON'T TOUCH BELOW THIS LINE --


def main():
    stack = Stack()
    size_stack(stack)
    pop_stack(stack)
    fill_stack(stack, 10)
    peek_stack(stack)
    peek_stack(stack)
    peek_stack(stack)
    peek_stack(stack)
    pop_stack(stack)
    pop_stack(stack)
    pop_stack(stack)
    size_stack(stack)


def size_stack(stack):
    print("size: " + str(stack.size()))
    return stack


def pop_stack(stack):
    print("popping: " + str(stack.pop()))
    print(stack.items)
    return stack


def peek_stack(stack):
    print("peeking: " + str(stack.peek()))
    print(stack.items)
    return stack


def fill_stack(stack, num):
    random.seed(1)
    options = ["banana", "apple", "pear", "carrot", "celery"]
    cars = []
    for i in range(num):
        optionI = random.randint(0, len(options)-1)
        print("pushing: " + options[optionI])
        stack.push(options[optionI])
        print(stack.items)
    return stack


main()