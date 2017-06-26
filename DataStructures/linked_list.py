"""Linked List"""


class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def add(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        while current:
            if current.get_data() == data:
                return current
            else:
                current = current.get_next()
        return None

    def remove(self, data):
        current = self.head
        prev = None
        while current:
            if current.get_data() == data:
                if current == self.head:
                    self.head = current.get_next()
                else:
                    prev.set_next(current.get_next())
                return current
            prev = current
            current = current.get_next()
        return None

    def print(self):
        final = []
        current = self.head
        while current:
            final.append(str(current.get_data()))
            current = current.get_next()
        print('->'.join(final))

linked_list = LinkedList()

while True:
    default = """
    1. Add
    2. Size
    3. Search
    4. Remove
    5. Print the Linked list
    """
    print(default)
    option = int(input("Select any option"))

    if option == 1:
        element = input("\nEnter the element you want to add")
        linked_list.add(element)

    if option == 2:
        print(linked_list.size())

    if option == 3:
        item = input("\nEnter the element you want to search")
        print(linked_list.search(item))

    if option == 4:
        data1 = input("\nEnter the element you want to search")
        linked_list.remove(data1)

    if option == 5:
        linked_list.print()
