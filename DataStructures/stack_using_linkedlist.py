"""Stack using Linked List"""


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        item = self.head.get_data()
        self.head = self.head.get_next()
        return item

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.head.get_data()

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def print(self):
        final = []
        current = self.head
        while current:
            final.append(str(current.get_data()))
            current = current.get_next()
        print('->'.join(final))

stack = Stack()

while True:
    default = """
    1. Push
    2. Pop
    3. Peek
    4. Size
    5. Print the Linked list
    """
    print(default)
    option = int(input("Select any option"))

    if option == 1:
        element = input("\nEnter the element you want to add")
        stack.push(element)

    if option == 2:
        print("\nThe element is", stack.pop())

    if option == 3:
        print("\n",stack.peek())

    if option == 4:
        print("\nSize of the stack is", stack.size())

    if option == 5:
        stack.print()


