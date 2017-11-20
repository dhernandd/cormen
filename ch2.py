# Copyright 2017 Daniel Hernandez Diaz, Columbia University
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

# CH. 2: BASIC SORTS

class InsertionSort(object):
    """
    """
    def __init__(self, l):
        """
        """
        self.List = l
        
    
    def isort(self):
        """
        """
        for j in range(1, len(self.List)):
            k = self.List[j]
            i = j - 1
            while i >= 0 and self.List[i] > k:
                self.List[i+1] = self.List[i]
                i = i - 1
            self.List[i+1] = k
                
            

class MergeSort():
    """
    """
    def __init__(self, l):
        """
        """
        self.List = l
        
    def merge(self, L1, L2):
        i = 0
        j = 0
        final = [0]*(len(L1) + len(L2)) # initialize a list that will contain the ordered values
        while i < len(L1) and j < len(L2): # i and j are walkers through lists L1 and L2 respectively
#             print i, j
            if L1[i] <= L2[j]: # if L1[i] <= L2[j] add L1[i] to final and advance in L1
                final[i+j] = L1[i]
                i += 1
            else:   # else, add L2[j] to final and advance in L2
                final[i+j] = L2[j]
                j += 1
        final[i+j:] = L1[i:] if j == len(L2) else L2[j:]
        return final
    
    
    def msort(self, L):
        if len(L) <= 1:
            return L
        else:
            r = len(L)/2
            L1, L2 = self.msort(L[:r]), self.msort(L[r:])
            return self.merge(L1, L2)
        


if __name__ == '__main__':
    isort = InsertionSort([3, 6, 9, 4, 1])
    isort.isort()
#     print isort.List
    
    msort = MergeSort([5, 3, 7, 2, 8, 1, 47, 9, 4, 82])
    print msort.msort([3, 1, 2, 0])
    
    