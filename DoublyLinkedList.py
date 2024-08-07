class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert_at_first(self, data):
        node = Node(data)
        if  self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1
    
    
    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1
        
    
    def insert_before(self, data, target):
        node = Node(data)
        if self.head.data == target:
            node.next = self.head
            self.head.prev = node
            self.head = node
            return
        
        current = self.head
        prev = self.head
        while current:
            if current.data == target:
                current.prev = node
                node.next = current
                node.prev = prev
                prev.next = node
                self.size += 1
                return 
            prev = current
            current = current.next

        else:
            raise Exception("Target not found")



    def display(self):
        current = self.head
        while current:
            if current.next == None:
                print(current.data)
            else:
                print(current.data, end=', ')
            current = current.next
        
        
nums = DoublyLinkedList()

for i in range(1,5):
    nums.append(i)

nums.display()
nums.insert_at_first(0)
nums.display()
nums.insert_before(5, 4)
nums.display()