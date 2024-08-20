class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    
    def arrange(self):
        node_index = self.size
        parent_index = node_index // 2
        while parent_index:
            if self.heap[node_index] < self.heap[parent_index]: 
                self.heap[node_index], self.heap[parent_index] = self.heap[parent_index], self.heap[node_index]
                parent_index //= 2
            else:
                break
            
    
    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange()
    
heap = MinHeap()
heap.insert(3)
heap.insert(1)
heap.insert(2)
heap.insert(4)
print(heap.heap)
        
        
