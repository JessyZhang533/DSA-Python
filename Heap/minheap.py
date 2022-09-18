# Min Heap:parent 
# 1.Basically a complete tree. Must be filled from left to right and every level must be full, with the exception of the last level not needing to be full.
# 2.'Min':every parent's key must be smaller than its children node.

class MinHeap:
    def __init__(self, capacity):
        " Constructor "
        self.values = [0] * capacity  # Store the values of each node
        self.capacity = capacity
        self.size = 0  # The number of elements stored in the heap

    # Helper methods
    def getParentIndex(self, index):
        " Given the index of a node, return the index of its parent "
        return (index - 1)//2

    def getLeftChildIndex(self, index):
        " Given the index of a node, return the index of its left child "
        return index * 2 + 1

    def getRightChildIndex(self, index):
        " Given the index of a node, return the index of its right child "
        return index * 2 + 2

    def hasParent(self, index):
        " Check if a given node has a parent "
        return self.getParentIndex(index) < self.size  # This is a boolean: True or False

    def hasLeftChild(self, index):
        " Check if a given node has a left child "
        return self.getLeftChildIndex(index) < self.size  # This is a boolean: True or False

    def hasRightChild(self, index):
        " Check if a given node has a right child "
        return self.getRightChildIndex(index) < self.size  # This is a boolean: True or False

    def value_parent(self, index):
        " Given the index of a node, return the value of its parent "
        return self.values[self.getParentIndex(index)]

    def value_leftchild(self, index):
        " Given the index of a node, return the value of its left child "
        return self.values[self.getLeftChildIndex(index)]

    def value_rightchild(self, index):
        " Given the index of a node, return the value of its right child "
        return self.values[self.getRightChildIndex(index)]

    def isFull(self):
        " See if there is still room for insertion "
        return self.size == self.capacity

    def swap(self, index1, index2):
        " Swap two nodes "
        temp = self.values[index1]
        self.values[index1] = self.values[index2]
        self.values[index2] = temp
    # Helper methods end

    def insert(self, data):
        " Insert a new node into the heap "
        if self.isFull():
            raise("The heap is full. Cannot insert")
        self.values[self.size] = data
        self.size += 1
        self.HeapUp()

