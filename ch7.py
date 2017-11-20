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

## CHAPTER 7. QUICKSORT


def quicksort(A, i=None, f=None):
    """
    TODO:
    """
    if i is None: i = 0
    if f is None: f = len(A)-1
    if i < f:
        q = partition(A, i, f)
        
        quicksort(A, i, q-1)
        quicksort(A, q+1, f)
    return A


def partition(A, ini, pivot):
    """
    Quicksort uses three markers in the array.
    
    pivot:         is the last element of the array with respect to which 
                   the other elements of the array are compared 
    low, high:     low, high determine an interval (low, high] of array
                   indices. All the elements inside of (low, high] are larger than pivot.
                   Elements lower than pivot are placed before low.
    """
    # The last element is taken as a pivot
    p = A[pivot]
    low = ini - 1
    for high in range(ini, pivot):
        if A[high] <= p:
            # Move an element smaller than pivot to right outside the
            # (low, high] interval
            low += 1
            A[high], A[low] = A[low], A[high]
    # Finally, insert the pivot as the first element of (low, high]
    A[low+1], A[pivot] = A[pivot], A[low+1]
    
    return low+1


if __name__ == '__main__':
    import numpy
    randints = numpy.random.randint(1, 1000, size=50)
    
    print randints
    A = quicksort(randints)
    print A

    
    