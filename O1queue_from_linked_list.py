class Queue:
    def remove_from_head(self):
        if self.head == None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            return temp
# add to head is not used as we can only add to tail in queue. 
    def add_to_head(self, node):
        if self.head == None:
            self.head = node
            return
        node.set_next(self.head)
        self.head = node

    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val


def main():
    queue = Queue()
    queue.add_to_tail(Node('lane'))
    print(queue)
    queue.add_to_tail(Node('preston'))
    print(queue)
    queue.add_to_tail(Node('rory'))
    print(queue)
    queue.add_to_tail(Node('ashley'))
    print(queue)
    print(queue.remove_from_head())
    print(queue)
    print(queue.remove_from_head())
    print(queue)
    print(queue.remove_from_head())
    print(queue)
    print(queue.remove_from_head())
    print(queue)


main()