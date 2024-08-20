class MaxHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0


    def arrange(self):
        index = self.size
        while index > 1 :
            if self.heap[index] > self.heap[index//2]: 
                self.heap[index], self.heap[index//2] = self.heap[index//2], self.heap[index]
                index //= 2
            else:
                break
            
    
    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange()
    
    
    def max_child(self, k):
        if (k * 2 + 1 > self.size) or (self.heap[k*2] > self.heap[k*2+1]):
            return k * 2
        else:
            return k * 2 + 1
        
        
    def sink(self, k):
        while k * 2 <= self.size:
            max_child = self.max_child(k)
            if self.heap[k] < self.heap[max_child]:
                self.heap[k], self.heap[max_child] = self.heap[max_child], self.heap[k]
                k = max_child
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
    
    heap = MaxHeap()
    for i in (1, 4, 2, 6, 3, 9, 10, 5, 7, 8):
        heap.insert(i)
    heap.display()
    heap.insert(11)
    heap.display()

    heap.delete_root()
    heap.display()

    heap.delete_at(2)
    heap.display()