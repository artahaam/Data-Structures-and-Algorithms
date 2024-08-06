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
        current = self.head
        prev = self.head
        node = Node(data)
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
        if count < index:
            raise Exception("List index out of range")

        
    def insert_before(self, data, target):
        current = self.head
        prev = self.head
        node = Node(data)
        flag = False
        while current:
            if current.data == target:
                node.next = current
                prev.next = node
                flag = True
                self.size += 1
            prev = current
            current = current.next
        if not flag:
            raise Exception("The target does not exist")
        
        
    def delete_first(self):
        if self.head is None:
            raise Exception("Nothing to delete")
        self.head = self.head.next
            
        
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
        counter = 0
        current = self.head
        prev = self.head
        while current:
            if counter == index:
                if current == self.head:
                    self.head = self.head.next
                else:
                    prev.next = current.next
                    self.size -= 1
                return
            prev = current
            current = current.next
            counter += 1
        if counter < index:
            raise Exception("Index out of range")
                    
        
    def clear(self):
        self.tail = None
        self.head = None


    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


    def search(self, data):
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
            


if __name__ == '__main__':

    numbers = SinglyLinkedList()
    
    for i in range(1, 10):
        numbers.append(i)
     
       
    numbers.display()

    numbers.delete_at(1)

    numbers.display()
    
    numbers.insert_at(0, 1)

    numbers.display()