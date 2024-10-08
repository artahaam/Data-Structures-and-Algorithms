class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
        
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        
        
    def push(self, data):
        node = Node(data)
        
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
            self.top.next = None
        self.size += 1
        
        
    def pop(self):
        if self.top:
            data = self.top.data
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            self.size -= 1
            return data
        else:
            raise Exception("empty Stack")


    def peek(self):
        if self.top:
            return self.top.data
        else:
            raise Exception("empty Stack")
    
    
    def clear(self):
        self.__init__()


    def display(self):
        current = self.top
        while current:
            if current.next == None:
                print(current.data, end='\n')
            else:
                print(current.data, end=', ')
            current = current.next

    
if __name__ == '__main__':
    # creating a Stack object            
    s = Stack()

    # pushing some items to the Stack
    for i in range(10):
        s.push(i)
    s.display()

    # pop some items
    s.pop()
    s.display()

    # getting the top item data
    print(s.peek())

    s.display()

    for i in range(3):
        s.pop()
    s.display()

    # poping the last item
    s.pop()
    s.display()

    s.clear()
    s.display()