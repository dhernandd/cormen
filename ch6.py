# Copyright 2017 Daniel Hernandez Diaz
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ==============================================================================

## CHAPTER 6. HEAPSORT

class Heap():
    """
    """
    def __init__(self, A):
        """
        """
        self.A = A
        
    
    def parent(self, i):
        if i == 0:
            return None
        else:
            return (i-1)/2
    
    
    def left_child(self, i):
        return 2*i+1
    
    
    def right_child(self, i):
        return 2*i+2
    
    
class MaxHeap(Heap):
    """
    TODO:
    """
    def __init__(self, A):
        """
        TODO:
        """
        Heap.__init__(self, A)
        
        self.build_max_heap()

    
    def max_heapify(self, index):
        A = self.A
        left = self.left_child(index)
        right = self.right_child(index)
        
        # Find the largest element between A[index] and its two children
        if left <= len(A)-1 and A[left] > A[index]:
            # If index is not a leaf and its left child is bigger
            L = left
        else: L = index
        if right <= len(A)-1 and A[right] > A[L]:
            # Compare now with index's right child if there is one.
            L = right
        
        # If A[index] is not the largest element, exchange it with the largest
        # of its children and recursively call max_heapify.
        if L != index:
            A[index], A[L] = A[L], A[index]
            self.max_heapify(L)
        
    
    def build_max_heap(self):
        heap_size = len(self.A)
        # Apply max_heapify for every non-leaf node
        for idx in range(heap_size/2-1, -1, -1):
            self.max_heapify(idx)
        
    
    def heapsort(self):
        """
        TODO:
        """
        tempA = [self.A[0]]
        # Exchange first and last element. It is necessary to remove the highest
        # element this way not to alter the heap structure.
        self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0] 
        for _ in range(len(self.A), 1, -1):
            self.A = self.A[:-1]
            self.max_heapify(0)
            tempA = tempA + [self.A[0]]
            self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
        
        self.A = tempA
        
        
        
if __name__ == '__main__':
    heap = MaxHeap([1, 34, 54, 2, 6, 32, 4, 893, 29, 20, 58])
    
    import numpy
    randints = numpy.random.randint(1, 1000, size=50)
    
    print 'Parent of Heap[0], Heap[7]:', heap.parent(0), heap.parent(7)
    print 'Left child of Heap[3]:', heap.left_child(3)
    print 'Right child of Heap[4]:', heap.right_child(4)
    
#     heap.max_heapify(0)
    print 'A max heap:', heap.A
    heap.heapsort()
    print 'Heapsort:', heap.A
    
    heapB = MaxHeap(randints)
    heapB.heapsort()
    print 'Heapsort:', heapB.A