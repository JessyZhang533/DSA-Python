# Min Heap:
# 1.Basically a complete tree. Must be filled from left to right and every level must be full, with the exception of the last level not needing to be full.
# 2.'Min':every parent must be smaller than its children.
# 3.The element removed should always be the root (the item on top of a real heap)

class MinHeap:
    def __init__(self, capacity):
        " Constructor "
        self.values = [0] * capacity  # Store the values of each node
        self.capacity = capacity
        self.size = 0  # The number of elements stored in the heap

    # Helper methods (same as max heap)
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

    # Insertion--time complexity: O(logn)
    def insert(self, data):
        " Insert a new node into the heap "
        if self.isFull():
            raise("The heap is full. Cannot insert")
        self.values[self.size] = data
        self.size += 1
        self.HeapifyUp(self.size - 1)  # In the bracket is the index of the newly inserted item

    def HeapifyUp(self, index):
        " Compare the value of the newly inserted to that of its parent; swap them if needed "
        if (self.hasParent(index) and self.value_parent(index) > self.values[index]):
            self.swap(self.getParentIndex(index), index)
            self.HeapifyUp(self.getParentIndex(index))  # Recursion

    # Removal--time complexity: O(logn)
    def remove(self):
        " Remove the minimum from the heap and return it "
        if self.size == 0:
            raise("Empty Heap.Cannot remove")
        data = self.values[0]
        self.values[0] == self.values[self.size - 1]  # Let the item last inserted be the head
        self.size -= 1
        self.HeapifyDown(0)
        return data

    def HeapifyDown(self, index):
        " Compare the value of the newly inserted to that of its children; swap them if needed "
        if (self.hasLeftChild(index) and self.values[index] > self.value_leftchild(index)):
            self.swap(self.getLeftChildIndex(index), index)
            self.HeapifyDown(self.getLeftChildIndex(index))
        if (self.hasRightChild(index) and self.values[index] > self.value_rightchild(index)):
            self.swap(self.getRightChildIndex(index), index)
            self.HeapifyDown(self.getRightChildIndex(index))


# Heap sort--O(nlogn)
def Heap_sort(list):
    " Sort a list of values from largest to smallest using the concept of heap "
    list_heap = MinHeap(len(list))
    list_sorted = []
    for i in list:  # O(logn)
        list_heap.insert(i)
    for _ in range(len(list_heap)):
        item_removed = list_heap.remove()
        list_sorted.append(item_removed)
    return list_sorted
