# list-based Queue
class ListQueue:
    def __init__(self):
        self.items = []
        self.front = self.rear = 0
    
    
    def enqueue(self, data):
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
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
        
    def enqueue(self, data):
        node = Node(data)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            node.next = self.rear
            self.rear.prev = node
            self.rear = node
        self.size += 1
        
        
    def dequeue(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        else:
            self.front = self.front.prev
            if self.size > 1:
                self.front.next = None
            else:
                self.front = self.rear = None
            self.size -= 1
    

    def display(self):
        if self.size == 0:
            print()
        current = self.rear
        count = self.size
        while current:
            if current.next == None:
                print(current.data, end='\n')
            else:
                print(current.data, end=', ')
            current = current.next
            count -= 1
        
        

#-------------------- ListQueue --------------------

# creating a ListQueue object
listqueue = ListQueue()

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



#-------------------- LinkedListQueue --------------------

# creating a Queue object
queue = Queue()

# enqueue some item
for i in range(5):
    queue.enqueue(i)
queue.display()

# dequeue some item
queue.dequeue()
queue.display()
queue.dequeue()
queue.display()
queue.dequeue()
queue.display()
