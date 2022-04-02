# Binary Search Tree - Delete
# Assignment
# Implement the delete method. It should take a value as an input and delete the node with that value if it exists. 
# In doing so, it will return the new value of the node (itself).

# Here are the steps:

# If self is None, just return None
# Otherwise, if the value to delete is less than the node's value, set the node's left child to the result of a recursive call to the delete method on the left subtree. Then return self.
# Otherwise, if the value to delete is greater than the node's value, set the node's right child to the result of a recursive call to the delete method on the right subtree. Then return self.
# Otherwise the given value and the node's value must be equal, meaning we've found the node we need to delete!
# If the node to delete has no right child, just return the left child
# If the node to delete has no left child, just return the right child
# If the node to delete has both children, we need to be more clever.
# Find the node with the smallest value in the node's right subtree
# Overwrite the current node's value with that smallest value
# Delete the node with the smallest value from the right subtree

import random


class BSTNode(object):

    def delete(self, val):
        if self.val == None:
            return None
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

        
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
    nums = get_nums(25)
    bst = BSTNode(12)
    for num in nums:
        bst.insert(num)
    print(bst)
    print("#")

    nums = [2, 6, 20]
    print("deleting " + str(nums))
    for num in nums:
        bst.delete(num)
    print(bst)


main()
