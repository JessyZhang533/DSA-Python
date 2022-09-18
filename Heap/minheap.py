# Min Heap:parent 
# 1.Basically a complete tree. Must be filled from left to right and every level must be full, with the exception of the last level not needing to be full.
# 2.'Min':every parent's key must be smaller than its children node.

class MinHeap:
    def __init__(self, capacity):
        " Constructor "
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0  # The number of elements stored in the heap
