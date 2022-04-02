
import random


class BSTNode(object):
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val


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
    nums = get_nums(40)
    bst = BSTNode(20)
    for num in nums:
        bst.insert(num)
    print(bst.get_min())
    print(bst.get_max())


main()