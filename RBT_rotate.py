# Let's write the rotate_left and rotate_right methods for our red black tree. 
# These methods will be fundamental to the "fix" method that we will implement in the next assignment.
# The rotations are what keep our tree balanced. Every time one branch of the tree starts to get too long, 
# we will just rotate those branches in order to keep the tree shallow. A shallow tree is a healthy (fast) tree!
# A properly-ordered tree pre-rotation remains an
# properly-ordered tree post-rotation
# In a rotation, one subtree becomes one level closer to
# the root and the other subtree becomes one level further from the root
# Rotations are O(1) operations

# Assignment
# Implement the rotate_left class method. It takes a single node, x as the input and rotates the tree around that node. The steps are as follows:
# Let y be x's right child.
# Set x's right child to be y's left child.
# If y's left child isn't a leaf node, set y's left-child's parent to x
# Set y's parent to x's parent
# If x is the root, set the root to y
# Otherwise, if x is its parent's left child, set x's parent's left child to y
# Otherwise, if x is its parent's right child, set x's parent's right child to y
# Set y's left child to be x
# Set x's parent to be y
# Implement the same algorithm for rotate_right with all the directionality inverted

import random
import sys, os
import time

class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def rotate_left(self, x):
        # print(f"x={x.val}")
        y = x.right
        # print(f"setting y to x.right, y = {x.right.val}")
        # print(f"setting new value for x.right to y.left,  y.left = {y.left.val}")
        x.right = y.left
        # print(f"new x.right (set to y.left in previous step)= {x.right.val}")
        if y.left != self.nil:
            # print(f"y.left is not self.nil, y.left.val = {y.left.val}")
            # print(f"y.left.parent = {y.left.parent.val}")
            y.left.parent = x
            # print(f"y.left.parent after setting it to x, y.left.parent = {y.left.parent.val}")
        # print(f"setting y.parent to x.parent..so y will have x's parent")
        y.parent = x.parent
        if x == self.root:
            # print(f"x was a root. root value = {self.root.val}")
            self.root = y
            # print(f"set new root to y, now the root value = {self.root.val}")
        elif x == x.parent.left:
            # print(f"pivot point x was not root, it was left child of its parent.{x.parent.left.val}")
            x.parent.left = y
        elif x == x.parent.right:
            # print(f"pivot point x was not root, it was left child of its parent.{x.parent.right.val}")
            x.parent.right = y
        # print("setting x as the left child of y")
        y.left = x
        # print(f"y.left = {y.left.val}")
        # print("setting parent of x to be y")
        x.parent = y
        # print(f"new parent of x = {x.parent.val}")


        



    def rotate_right(self, x): #x is pivot
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x == self.root:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        elif x == x.parent.right:
            x.parent.right = y
        y.right = x
        x.parent = y




        # -- TEST SUITE, DON'T TOUCH BELOW THIS LINE --
    def insert(self, val):
        # Ordinary Binary Search Insertion
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return

        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

    def __repr__(self):
        lines = []
        print_tree(self.root, lines)
        return '\n'.join(lines)


def print_tree(node, lines, level=0):
    if node.val != 0:
        print_tree(node.left, lines, level + 1)
        lines.append('-' * 4 * level + '> ' +
                     str(node.val) + ' ' + ('r' if node.red else 'b'))
        print_tree(node.right, lines, level + 1)


def get_nums(num):
    random.seed(1)
    nums = []
    for _ in range(num):
        nums.append(random.randint(1, num-1))
    return nums


def main():
    os.system("cls")
    time.sleep(1)
    nums = get_nums(25)
    tree = RBTree()
    for num in nums:
        tree.insert(num)
    print(tree)

    print("#")
    print("rotating left at 5")
    print("#")
    tree.rotate_left(tree.root)
    print(tree)

    print("#")
    print("rotating right at 21")
    print("#")
    tree.rotate_right(tree.root.right)
    print(tree)


main()