"""Implement a Stack using Linked List"""


class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next_node = None


class Stack(object):

    def __init__(self):
        self.head = None

    def enqueue(self, item):
        temp = Node(item)
        temp.next_node = item
        self.head = temp

    def dequeue(self):
            return self.head.data[1]

    def peek(self):
        return self.head.data

    def isempty(self):
        return self.head is None

    def size(self):
        count = 0


stack = Stack()
stack.enqueue(12)
stack.enqueue(13)
stack.enqueue(14)
stack.enqueue(15)
print(stack.dequeue())
print(stack.size())
