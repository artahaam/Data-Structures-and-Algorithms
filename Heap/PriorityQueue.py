from MinHeap import MinHeap

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class MinPriorityQueue:
    def __init__(self):
        self.heap = MinHeap()
        self.objects = {}
        
        
    def instert(self, key, value):
        node = Node(key, value)
        self.objects[key] = value
        self.heap.insert(key)
    
    
    def extract_min(self):
        return self.heap.extract_min()
    
    
    def display(self):
        for key in self.heap.sort():
            print(self.objects[key], end=', ')


mpq = MinPriorityQueue()

mpq.instert(1, 'a')
mpq.instert(2, 'b')
mpq.instert(3, 'c')
mpq.display()
print(mpq.extract_min())
mpq.display()
        
