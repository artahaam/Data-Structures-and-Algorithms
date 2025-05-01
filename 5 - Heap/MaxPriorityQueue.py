from MaxHeap import MaxHeap

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class MaxPriorityQueue:
    def __init__(self):
        self.heap = MaxHeap()
        self.objects = {}
        self.keys = set()
        
        
    def instert(self, key, value):
        if key in self.keys:
            raise Exception("two objects can't have same priority")
        else:
            self.keys.add(key)
        self.objects[key] = value
        self.heap.insert(key)
    
    
    def extract_max(self):
        return self.objects[self.heap.extract_max()]
    
    
    def display(self):
        for key in self.heap.sort():
            print(key, self.objects[key])
        print()


if __name__ == '__main__':

    mpq = MaxPriorityQueue()

    mpq.instert(1, 'Reza')
    mpq.instert(3, 'Shervin')
    mpq.instert(2, 'Naser')
    mpq.instert(0, 'Maral')
    mpq.display()

    for i, j in [
                (66, 'Hasan Shamaeizade'),
                (55, 'Ebrahim Raesi'),
                (6, 'Mohsen Lorestani'),
                (38, 'Mahmoud Ahmadinejad'),
                (50, 'Siavash Ghomeishi'),
                (31, 'Reza Ghoushannejad'),
                (28, 'Mohsen Yegane'),
                (49, 'Hashemi Rafsanjani'),
                (93, 'Googoosh'),
                (72, 'Ebi'),
                ]:
        
        mpq.instert(i, j)

    mpq.display()
        

    print(mpq.extract_max())
            
