def swap(my_list, index1, index2):
    " Swap the position of two items in a list "
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    " Group the items smaller than pivot on its left & items greater than pivot on its right; return the pivot index "
    swap_index = pivot_index  # Here we store the index instead of the value
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1  # swap_index+1 always points to the first item greater than pivot
            swap(my_list, i, swap_index)  # swap my_list[i], which is less than pivot, withthe first item greater than pivot
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list, left, right):
    " Recursively find pivot and regroup the list until the list is sorted "
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list


def quick_sort(my_list):
    " Simplified argument "
    return quick_sort_helper(my_list, 0, len(my_list)-1)


my_list = [5, 3, 9, 1, 6, 7, 8, 0]
print(pivot(my_list, 0, 7))
print(my_list)
print(quick_sort(my_list))
