# list-based Queue
class ListQueue:
    def __init__(self, size):
        self.items = []
        self.front = self.rear = 0
        self.size = size
    
    
    def enqueue(self, data):
        if self.size == self.rear:
            raise Exception("Queue is full")
        else:
            self.items.insert(0, data)
            self.front += 1
            
    
        
    def dequeue(self):
        if self.front == self.rear:
            raise Exception("Queue is empty")
        else:
            data = self.items.pop()
            self.front -= 1
        return data
        

    
    
    
# Linkedlist-based Queue
class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
# Stack-based Queues