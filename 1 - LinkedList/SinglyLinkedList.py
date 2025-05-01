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
        
    # index handling
    def index_handler(self, index):
        if index >= self.size:
            raise Exception("Index out of range")
        elif index < 0:
            index = self.size + index
            return index 
        else:
            return index
    
    # append
    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1
        
    # insert item at a specefic index
    def insert_at(self, data, index):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
            return
        index = self.index_handler(index)
        if index == self.size:
            self.append(data)
            self.size += 1
            return
        else:
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

    # insert item before a specific item
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
        
    # delete the front item
    def delete_first(self):
        if self.head is None:
            raise Exception("Nothing to delete")
        self.head = self.head.next
        self.size -= 1
            
    # delete the back item
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
                
    # delete item by value
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
        
    # delete item at a specific index
    def delete_at(self, index):
        index = self.index_handler(index)
        if  index == 0 and self.size == 1:
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

    # clearing the whole list
    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0

    # iterating through list items
    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    # check if an item exists in list by value
    def contains(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False
    
    # display list
    def display(self):
        if self.size == 0:
            print()
            return
        else:
            current = self.head
            while current:
                if current.next == None:
                    print(current.data, end='\n')
                else:
                    print(current.data, end=', ')
                current = current.next
        

if __name__ == '__main__':

    # creating SinglyLinkedLit object
    numbers = SinglyLinkedList()
    
    # appending some item to List
    for i in range(4, 8):
        numbers.append(i)
    numbers.display()
    
    # inserting at front
    numbers.insert_at(3, 0)
    numbers.display()
    
    # inserting at back
    numbers.insert_at(9, -1)
    numbers.display()
    
    # insert intermediate 
    numbers.insert_at(8, -2)
    numbers.display()
    
    # insert before item
    numbers.insert_before(2, 3)
    numbers.display()
    
    # delete front item
    numbers.delete_first()
    numbers.display()
    
    # delete back item
    numbers.delete_last()
    numbers.display()
    
    # delete first item
    numbers.delete(3)
    numbers.display()
    
    # delete intermediate item
    numbers.delete(5)
    numbers.display()
    
    # delete last item
    numbers.delete(9)
    numbers.display()
    
    # check if list contains a specific item
    print(numbers.contains(3))
    print(numbers.contains(4))
    
    # clearing the list
    numbers.clear()
    numbers.display()
    
