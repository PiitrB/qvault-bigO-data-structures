# Binary Search Tree - Traverse Inorder
# Assignment
# Implement the recursive inorder method. It returns a list of the values in the order they are visited, and it takes as an argument the ordering of values visited so far.
# For example, the first call to inorder on an entire tree would be:
# # an empty list is passed in the first call
# bst_node.inorder([])
# Here are the algorithm's steps:
# Recursively traverse the left subtree
# Visit the value of the current node by pushing it's value onto the visited array
# Recursively traverse the right subtree
# Return the list of nodes visited so far
# The following tree:
#          > 1 
#      > 2 
#  > 4 
#          > 6 
#      > 7 
# Would return the following list:
# [1, 2, 4, 6, 7]

import random


class BSTNode(object):

    def inorder(self, visited):
        if self.val == None:
            return []
        if self.left:
            self.left.inorder(visited)
        visited.append(self.val)    
        if self.right:
            self.right.inorder(visited)
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
    print("inorder:")
    print(bst.inorder([]))
    print("#########")

    nums = get_nums(25)
    bst = BSTNode(12)
    for num in nums:
        bst.insert(num)
    print(bst)
    print("#########")
    print("inorder:")
    print(bst.inorder([]))


main()
