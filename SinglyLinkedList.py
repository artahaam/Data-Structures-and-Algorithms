class Node:
    def __init__ (self, data=None):
        self.data = data
        self.next = None


    def __str__(self):
        return self.data


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def index_handler(self, index):
        if index >= self.size:
            raise Exception("Index out of range handler")
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
        else:
            self.head = node
            self.tail = node
        self.size += 1
        
    
    def insert_at(self, data, index):
        index = self.index_handler(index)
        if index == self.size:
            self.append(data)
            self.size += 1
            return
        node = Node(data)
        current = self.head
        prev = self.head
        count = 0
        while current :
            if index == 0:
                node.next = current
                self.head = node
                self.size += 1
                return 
            elif count == index:
                node.next = current
                prev.next = node
                self.size += 1 
                return
            count += 1
            prev = current 
            current = current.next

        
    def insert_before(self, data, target):
        node = Node(data)
        if self.head.data == target:
            node.next = self.head
            self.head = node
            self.size += 1
            return 
        current = self.head
        prev = self.head
        flag = False
        while current:
            if current.data == target:
                node.next = current
                prev.next = node
                flag = True
                self.size += 1
                return
            prev = current
            current = current.next
        if not flag:
            raise Exception("Target not found")
        
        
    def delete_first(self):
        if self.head is None:
            raise Exception("Nothing to delete")
        self.head = self.head.next
        self.size -= 1
            
        
    def delete_last(self):
        current = self.head 
        prev = self.head    
        while current:
                if current.next is None:
                    prev.next = None
                    self.size -= 1
                    return
                prev = current
                current = current.next
                
                
    def delete(self, data):
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = self.head.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
        else:
            raise Exception("Nothing to delete")
        
        
    def delete_at(self, index):
        index = self.index_handler(index)
        if index == self.size-1:
            self.tail = None
            self.head = None
            self.size = 0
            return
        counter = 0
        current = self.head
        prev = self.head
        while current:
            if counter == index:
                if current == self.head:
                    self.head = self.head.next
                    self.size -= 1
                else:
                    prev.next = current.next
                    self.size -= 1
                return
            prev = current
            current = current.next
            counter += 1

        
    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0


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
                print(current.data,)
            else:
                print(current.data, end=', ')
            current = current.next
            


if __name__ == '__main__':

    numbers = SinglyLinkedList()
    
    for i in range(0, 10):
        numbers.append(i)
    
    numbers.display()
    numbers.append(5)
    numbers.display()
    numbers.insert_before(3, 5)
    numbers.display()
    numbers.delete_first()
    numbers.display()
    numbers.delete_last()
    numbers.display()
    numbers.delete(2)
    numbers.display()
    numbers.insert_at(4, -2) 
    numbers.display()
    numbers.delete_at(2)
    numbers.display()
    numbers.insert_before(3, 1)
    numbers.display()
    print(numbers.contains(4))
    numbers.delete_at(0)
    numbers.display()
    numbers.delete_at(0)
    numbers.display()
    numbers.delete_at(0)
    numbers.display()
    numbers.insert_before(0, 3)
    numbers.display()
    numbers.insert_at(7, -2)
    numbers.display()
