class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return self.data

class DoublyLinkedList:
    def __init__(self):
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
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1
        
    
    def insert_before(self, data, target):
        node = Node(data)
        if self.head.data == target:
            node.next = self.head
            self.head.prev = None
            self.head = node
            self.size += 1
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

    
    def insert_at(self, data, index):
        index = self.index_handler(index)
        if index == self.size:
            self.append(data)
            return
        if index == 0 and self.size:
            self.insert_at_first(data)
            return
        node = Node(data)
        current = self.head
        prev = self.head
        count = 0
        while current:
            if count == index:
                node.next = current
                node.prev = prev
                current.prev = node
                prev.next = node
                if index == 0:
                    self.head = node
                self.size += 1
                return 
            prev = current
            current = current.next
            count += 1
        
        
    def delete(self, data):
        current = self.head
        deleted = False
        if current is None:
            raise Exception("empty list")
        elif current.data == data:
            self.head.prev = None
            self.head = current.next
            deleted = True
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            deleted = True
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    deleted = True
                current = current.next
        if deleted is False:
            raise Exception("target not found")
        else:
            self.size -= 1

        
    def delete_at(self, index):
        index = self.index_handler(index)
        if  index == 0 and self.size ==1:
            self.head = None
            self.size -= 1
            return
        elif index == self.size-1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
        else:
            current = self.head
            prev = self.head
            count = 0
            while current:
                if count == index:
                    if current == self.head:
                        self.head = current.next
                        self.size -= 1  
                        return 
                    elif current == self.tail:
                        self.tail.next = None
                        self.tail = current.prev
                        self.size -= 1  
                        return 
                    else:
                        prev.next = current.next
                        current.next.prev = prev
                        self.size -= 1
                        return
                count += 1
                prev = current
                current = current.next
    
    
    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val    

            
    def contains(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False


    def display(self):
        current = self.head
        while current:
            if current.next == None:
                print(current.data)
            else:
                print(current.data, end=', ')
            current = current.next            
        if self.size == 0:
            print()
        
    
if __name__ == '__main__':
    
    nums = DoublyLinkedList()
    
    for i in range(1,5):
        nums.append(i)
        
    nums.display()
    nums.insert_at_first(0)
    nums.display()
    nums.insert_at(0, 1)
    nums.display()
    nums.insert_at(0, 2)
    nums.display()
    nums.insert_before('k', 0)
    nums.display()
    nums.insert_before('k',4)
    nums.display()
    nums.delete('k')
    nums.display()
    nums.delete('k')
    nums.display()
    nums.delete_at(0)
    nums.display()
    nums.delete_at(4)
    nums.display()
    nums.delete_at(4)
    nums.display()
    nums.delete_at(3)
    nums.display()
    nums.delete_at(1)
    nums.display()
    nums.delete_at(1)
    nums.display()
    nums.delete_at(0)
    nums.display()