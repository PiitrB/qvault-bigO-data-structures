# Binary Search Tree - Traverse Preorder
# Sometimes it's useful, albeit a bit slow, to iterate over all the nodes in the tree, rather than searching for a specific one.
# In the next few assignments we will explore different ways of traversing a BST.
# Assignment
# Implement the recursive preorder method. It returns a list of the values in the order they are visited, and it takes as an argument the ordering of values we have visited so far.
# For example, the first call to preoder on an entire tree would be:
# # an empty list is passed in the first call
# bst_node.preorder([])
# Here are the algorithm's steps:

# Visit the value of the current node by appending it's value into the visited array
# Recursively traverse the left subtree
# Recursively traverse the right subtree
# Return the array of visited nodes
# The following tree:

#          > 1 

#      > 2 

#  > 4 

#          > 6 

#      > 7 
# Would return the following list:

# [4, 2, 1, 7, 6]

import random


class BSTNode(object):

    def preorder(self, visited):
        if self.val == None:
            return [] 
        visited.append(self.val)
        if self.left:
            self.left.preorder(visited)
        if self.right:
            self.right.preorder(visited)

        return visited


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
    nums = get_nums(8)
    bst = BSTNode(4)
    for num in nums:
        bst.insert(num)
    print(bst)
    print("#")
    print("preorder:")
    print(bst.preorder([]))
    print("#########")

    nums = get_nums(25)
    bst = BSTNode(12)
    for num in nums:
        bst.insert(num)
    print(bst)
    print("#########")
    print("preorder:")
    print(bst.preorder([]))


main()
