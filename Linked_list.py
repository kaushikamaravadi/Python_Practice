class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getdata(self):
        return self.data

    def getnext(self):
        return self.next

    def setdata(self,newdata):
        self.data = newdata

    def setnext(self,newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isempty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setnext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getnext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getdata() == item:
                found = True
            else:
                current = current.getnext()
        return item,found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getdata()== item:
                found = True
            else:
                previous = current
                current = current.getnext()
        if previous == None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())

linkedlist = UnorderedList()

linkedlist.add(31)
linkedlist.add(81)
linkedlist.add(61)
linkedlist.add(51)
linkedlist.add(41)

print(linkedlist.size())
print(linkedlist.remove(81))
print(linkedlist.search(61))
print(linkedlist.size())
print(linkedlist.remove(41))
print(linkedlist.size())




