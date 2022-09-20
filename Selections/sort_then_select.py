def sort_then_select(list, k):
    " Sort the list & index directly; return the kth smallest element in the array "
    list.sort()
    return list[k]


my_list = [4, 0, 9, 5, 7, 2]
print(sort_then_select(my_list, 3))  # Return the third smallest, should be 5
