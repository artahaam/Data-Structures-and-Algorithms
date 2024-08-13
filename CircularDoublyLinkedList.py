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
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
        else:
            self.head = node
            self.tail = node
            self.tail.next = self.head
            self.head.next = self.tail
        self.size += 1
        
        
    
    def delete(self, data):
        current = self.head
        deleted = False
        if current is None:
            raise Exception("empty list")
        elif current.data == data:
            self.head.prev = self.tail
            self.head = current.next
            self.tail.next = self.head
            deleted = True
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            deleted = True
        else:
            while current != self.tail:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    deleted = True
                current = current.next
        if deleted is False:
            raise Exception("target not found")
        else:
            self.size -= 1
        return
    
    
    def delete_at(self, index):
        index = self.index_handler(index)
        if  index == 0 and self.size == 1:
            self.tail = None
            self.head = None
            self.size = 0
            return
        current = self.head
        prev = self.head
        counter = 0
        while current == prev or prev != self.tail:
            if counter == index:
                if current == self.head:
                    self.head = self.head.next
                    self.tail.next = self.head
                    self.size -= 1
                else:
                    prev.next = current.next
                    self.size -=1 
                return
            prev = current
            current = current.next
            counter += 1


    def display(self):
        if self.size == 0:
            print()
            return
        else:
            current = self.head
            counter = 0
            while  counter < self.size:
                if current.next == self.head:
                    print(current.data)
                else:
                    print(current.data, end=', ')
                current = current.next
                counter += 1


if __name__ == '__main__':
    
    # create a CircularLinkedList object
    nums = CircularLinkedList()
    
    # appending some items to it
    for i in range(2,10):
        nums.append(i)
    nums.display()
        
    # deleting the first object
    nums.delete(2)
    nums.display()
    
    # deleting the last object
    nums.delete(9)
    nums.display()
    
    # deleting an intermediate object
    nums.delete(5)
    nums.display()
    
    # deleting at a specific index (first)
    nums.delete_at(0)
    nums.display()
    
    # deleting at a specific index (last)
    nums.delete_at(-1)
    nums.display()
    
    # deleting at a specific index (intermediate)
    nums.delete_at(1)
    nums.display()
