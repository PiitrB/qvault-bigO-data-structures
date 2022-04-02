# Stack Overflow
# Let's do a runtime stack simulation so we can better visualize how it works.

# I've provided a call() function that takes a function as input and executes it with some additional logging. Instead of calling each function in the normal way you can use the call function. For example:

# call(my_function)
# instead of:

# my_function()
# The call function will push and pop the name of the function on and off of our own Stack implementation, and will print the state of the stack at each step.

# Assignment
# Modify main to call functions one and two using call()
# Modify function_one to call function_three using call()

def main():
    call(function_one)
    call(function_two)


def function_one():
    call(function_three)


def function_two():
    pass


def function_three():
    pass


# -- TEST SUITE, DON'T TOUCH BELOW THIS LINE --
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
        return self.items[len(self.items)-1]


stack = Stack()


def call(func):
    stack.push(func.__name__)
    print("stack: "+str(stack.items))
    func()
    stack.pop()
    print("stack: "+str(stack.items))


call(main)
