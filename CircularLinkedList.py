class Node:
    def __init__ (self, data=None):
        self.data = data
        self.next = None


    def __str__(self):
        return self.data


class CircularLinkedList:
    def __init__ (self):
        self.tail = None
        self.head = None
        self.size = 0
    
    
    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
            node.next = self.head
        else:
            self.head = node
            self.tail = node
            self.tail.next = self.head
        self.size += 1
    
    
    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val
    
    
    def display(self):
        if self.size == 0:
            print()
            return
        else:
            current = self.head
            counter = 0
            while counter < self.size:
                if current.next == None:
                    print(current.data)
                else:
                    print(current.data, end=', ')
                current = current.next
                counter += 1
                
                
nums = CircularLinkedList()

for i in range(5):
    nums.append(i)

nums.display()