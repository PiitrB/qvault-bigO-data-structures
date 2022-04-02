# Binary Search Tree - Exists
# We need a method to check if a value already exists in the tree.

# Assignment
# Implement the exists method. It should take a value as input and return True if the value exists in the tree, and False if it doesn't.

import random

class BSTNode(object):

    def exists(self, val):
        if self == None:
            return False
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.val == val:
                return True
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return False


        # -- TEST SUITE, DON'T TOUCH BELOW THIS LINE --
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def __repr__(self):
        lines = []
        print_tree(self, lines)
        return '\n'.join(lines)


def print_tree(bst_node, lines, level=0):
    if bst_node != None:
        print_tree(bst_node.left, lines, level + 1)
        lines.append(' ' * 4 * level + '> ' + str(bst_node.val))
        print_tree(bst_node.right, lines, level + 1)


def get_nums(num):
    random.seed(1)
    nums = []
    for _ in range(num):
        nums.append(random.randint(0, num-1))
    return nums


def main():
    nums = get_nums(1000)
    bst = BSTNode(50)
    for num in nums:
        bst.insert(num)

    nums = get_nums(25)
    for num in nums:
        print(str(num) + " exists:")
        print(bst.exists(num))


main()
