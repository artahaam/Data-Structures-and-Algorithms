class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
        
    def __str__(self):
        return self.data


class CircularLinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0
        
        
    def index_handler(self, index):
        if index >= self.size:
            raise Exception("Index out of range")
        elif index < 0:
            index = self.size + index
            return index 
        else:
            return index
        
        
    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
        else:
            self.head = node
            self.tail = node
            self.tail.next = self.head
        self.size += 1