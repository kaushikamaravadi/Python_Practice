class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def print(self):
        return self.items

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
