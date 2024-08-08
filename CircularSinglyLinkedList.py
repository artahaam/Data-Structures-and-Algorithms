class Node:
    def __init__ (self, data=None):
        self.data = data
        self.next = None


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
    
    
    def delete(self, data):
        current = self.head
        prev = self.head
        deleted = False
        while prev == current or prev != self.tail:
            if current.data == data:
                if current == self.head:
                    self.tail.next = current.next
                    self.head = current.next
                elif current == self.tail:
                    prev.next = self.head
                    self.tail = prev
                else:
                    prev.next = current.next
                self.size -= 1
                deleted = True
                return
            prev = current
            current = current.next
        if not deleted:
            raise Exception("target not found")

    
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
                
    def insert(self, data, index):
        index = self.index_handler(index)
        current = self.head
        prev = self.head
        node = Node(data)
        counter = 0
        while current == prev or prev != self.tail:
            if counter == index:
                if current == self.head:
                    self.tail.next = node
                    self.head = node
                    self.head.next = current
                    self.size += 1
                    return
                elif current == self.tail:
                    self.tail.next = node
                    self.tail = node
                    self.tail.next = self.head
                    self.size += 1
                    return
                else:
                    prev.next = node 
                    node.next = current
                    self.size += 1
                    return            
            prev = current
            current = current.next
            counter += 1

                
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
            prev = self.head
            counter = 0
            while  prev != self.tail:
                if current.next == self.head:
                    print(current.data)
                else:
                    print(current.data, end=', ')
                prev = current
                current = current.next
                counter += 1

                
if __name__ == '__main__':
        
    nums = CircularLinkedList()

    for i in range(10):
        nums.append(i)

    nums.display()
    nums.delete(1)
    nums.display()
    nums.delete_at(1)
    nums.display()
    nums.insert(10, 0)
    nums.display()
    nums.insert(10, 8)
    nums.display()
    nums.insert(10, 9)
    nums.display()
    nums.insert(10, 4)
    nums.display()
