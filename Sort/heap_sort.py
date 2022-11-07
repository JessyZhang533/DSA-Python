def Heap_sort(list):
    " Sort a list of values from smallest to largest using the concept of heap "
    list_heap = MinHeap(len(list))
    list_sorted = []
    for i in list:  # O(logn)
        list_heap.insert(i)
    for _ in range(len(list)):
        item_removed = list_heap.remove()
        list_heap.print()
        list_sorted.append(item_removed)
    return list_sorted