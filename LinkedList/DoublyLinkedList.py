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
    
    # index handling
    def index_handler(self, index):
        if index >= self.size:
            raise Exception("Index out of range")
        elif index < 0:
            index = self.size + index
            return index 
        else:
            return index
    
    # insert an item at front of the list
    def insert_at_first(self, data):
        node = Node(data)
        if  self.head is None:
            self.head = node
            self.tail = node
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1
    
    # append items into the list
    def append(self, data):
        node = Node(data)
        if self.tail:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
            self.head.next = self.tail
            self.tail.prev = self.head
        self.size += 1
        
    # insert item before a specific item
    def insert_before(self, data, target):
        node = Node(data)
        if self.head.data == target:
            node.next = self.head
            self.head.prev = node
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
                current.prev = node
                node.prev = prev
                prev.next = node
                if index == 0:
                    node.next = self.head
                    self.head.prev = node
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
        if  index == 0 and self.size == 1:
            self.head = None
            self.tail = None
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
                        current.next.prev = self.head
                        self.size -= 1  
                        return 
                    elif current == self.tail:
                        self.tail.next = None
                        self.tail = prev 
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
        current = self.head
        while current:
            if current.next == None:
                print(current.data, end='\n')
            else:
                print(current.data, end=', ')
            current = current.next            

    
if __name__ == '__main__':
    
    # creating a DoublyLinkedList object
    nums = DoublyLinkedList()
    
    # appending some items to list
    for i in range(1,5):
        nums.append(i)
    nums.display()

    # insert at front
    nums.insert_at_first(0)
    nums.display()
    
    # insert before the first item
    nums.insert_before(5, 0)
    nums.display()
    
    # insert before an intermediate number
    nums.insert_before(5, 3)
    nums.display()
    
    # insert before the last item
    nums.insert_before(5, 4)
    nums.display()
    
    # insert at the front of the list
    nums.insert_at(4, 0)
    nums.display()
    
    # insert at the back of the list
    nums.insert_at(3, -1)
    nums.display()
    

    # delete data at front by value
    nums.delete(4)
    nums.display()
    
    # delete data at back by value
    nums.delete(4)
    nums.display()
    
    # delete the item at front
    nums.delete_at(0)
    nums.display()
    
    # delete the item at back
    nums.delete_at(6)
    nums.display()
    
    # delete an intermediate item   
    nums.delete_at(3)
    nums.display()
    
    # check if list contains a specific item
    print(nums.contains(3))
    print(nums.contains(4))
    