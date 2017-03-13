"""Queue"""

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print(self):
        return self.items

queue = Queue()

while True:
    default = """
    1. Enqueue
    2. Dequeue
    3. Empty the queue
    4. size
    5. Print the Linked list
    """
    print(default)
    option = int(input("Select any option"))

    if option == 1:
        element = input("\nEnter the element you want to add")
        queue.enqueue(element)

    if option == 2:
        print("\nThe element is", queue.dequeue())

    if option == 3:
        print("\n", queue.is_empty())

    if option == 4:
        print("\nSize of the stack is", queue.size())

    if option == 5:
        queue.print()
