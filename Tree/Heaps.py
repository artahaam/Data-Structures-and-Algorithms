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
    
    
    def min_child(self, k):
        if (k * 2 + 1 > self.size) or (self.heap[k*2] < self.heap[k*2+1]):
            return k * 2
        else:
            return k * 2 + 1
        
        
    def sink(self, k):
        while k * 2 <= self.size:
            min_child = self.min_child(k)
            if self.heap[k] > self.heap[min_child]:
                self.heap[k], self.heap[min_child] = self.heap[min_child], self.heap[k]
                k = min_child
            else:
                break

    
    def delete_root(self):
        item = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.size -= 1
        self.sink(1)
        return item
    
    
    def delete_at(self, index):
        item = self.heap[index]
        self.heap[index] = self.heap.pop()
        self.size -= 1
        self.sink(index)
        return item
        
    
    def display(self):
        print(self.heap[1:])
        
        
if __name__ =='__main__':
    
    heap = MinHeap()
    for i in (1, 4, 2, 6, 3, 9, 10, 5, 7, 8):
        heap.insert(i)
    heap.display()

    for i in range(5):
        print(heap.delete_root())
    heap.display()
    
    heap.delete_at(1)
    heap.display()
    
    heap.delete_at(3)
    heap.display()
    