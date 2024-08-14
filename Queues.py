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
        
    
    def count(self):
        return self.front

    
    def display(self):
        print(*self.items)
    
    
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


# creating a ListQueue object
listqueue = ListQueue(10)

# equeue some items to the queue
for i in range(6):
    listqueue.enqueue(i)

listqueue.display()

# dequeue some items from the queue
for i in range(3):
    listqueue.dequeue()
    listqueue.display()
    
# printing the number of items in the queue
print(listqueue.count())