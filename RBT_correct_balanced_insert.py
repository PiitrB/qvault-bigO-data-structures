# Red Black Tree - Fix Insert
# Let's finish strong by implementing the fix_insert method. When we're done here, we will have a fully functional (albeit insert-only) red-black tree. 
# As you can see if you look at the bottom of the test suite, we'll be inserting the numbers 1-50 into our tree in order. 
# A normal binary tree would break down into a single unruly branch:
# Normal BST (Unbalanced with ordered insertions)
# 1-|
#   2-|
#     3-|
#       4-|
#         ...
# Red-Black BST (Balanced with ordered insertions)
#        ...
#      4-|
#    8-|
#      12-|
# 16-|
#      20-|
#   24-|
#      32-|  
#        ...
# Assignment
# We need to modify the insert method slightly, let's do that first. At the end of what you have so far:
# If the new node is a root node, make it black and just return. There's nothing to fix.
# If the new node's grandparent is None just return. There's nothing to fix.
# Call the new fix_insert method with the new_node as the input
# We've already written the rotation functions, so the fix_insert method is mostly just responsible for recoloring the nodes, and calling the rotation methods when necessary.

# While the new node isn't the root of the tree and its parent is red:
#     If the parent is a right child:
#         Set uncle to the parent's sibling
#         If the uncle is red:
#             Change the uncle to black
#             Set the parent to black
#             Set the grandparent to red
#             Set the new node to be equal to the grandparent. This will allow the loop to continue the recoloring process up the tree
#         Otherwise, if the uncle is black:
#             If the new node is a left child:
#                 Set the new node to its parent
#                 Rotate the tree right around the new node
#         Set the parent to black
#         Set the grandparent to red
#         Rotate the tree left around the grandparent
#     Otherwise, if the parent is a left child:
#         Set uncle to the parent's sibling
#         If the uncle is red:
#             Change the uncle to black
#             Set the parent to black
#             Set the grandparent to red
#             Set the new node to its grandparent
#         Otherwise, if the uncle is black:
#             If the new node is a right child:
#                 Set the new node to its parent
#                 Rotate the tree left around the new node
#             Set the parent to black
#             Set the grandparent to red
#             Rotate the tree right around the grandparent
# Set the root to black

import random


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

    def insert(self, val):
        # Ordinary Binary Search Insertion
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True  # new node must be red

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

        # Set the parent and insert the new node
        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
        
        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            if new_node.parent.parent.right == new_node.parent:
                uncle = new_node.parent.parent.left
                if uncle.red: #if uncle is red
                    uncle.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else: #if uncle is black
                    if new_node.parent.left == new_node:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.right
                if uncle.red: #if uncle is red
                    uncle.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else: #if uncle is black
                    if new_node.parent.right == new_node:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)
        self.root.red = False



    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    # rotate left at node x
    def rotate_left(self, x):
        if x.right == None:
            return
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def rotate_right(self, x):
        if x.left == None:
            return
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

# -- TEST SUITE, DON'T TOUCH BELOW THIS LINE --
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
    tree = RBTree()
    for x in range(1, 51):
        tree.insert(x)
    print(tree)


main()
