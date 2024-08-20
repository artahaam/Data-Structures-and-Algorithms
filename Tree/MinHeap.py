class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    
    def arrange(self):
        index = self.size
        while index > 1 :
            if self.heap[index] < self.heap[index//2]: 
                self.heap[index], self.heap[index//2] = self.heap[index//2], self.heap[index]
                index //= 2
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
    # for i in (1, 4, 2, 6, 3, 9, 10, 5, 7, 8):
    for i in (10, 3, 1, 5, 4, 8, 9, 2, 6, 7):
        heap.insert(i)
        heap.display()
    heap.insert(0)
    heap.display()
    heap.insert(-1)
    heap.display()

    for i in range(5):
        print(heap.delete_root())
    heap.display()
    
