def swap(my_list, index1, index2):
    " Swap the position of two items in a list "
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    " Group the items smaller than pivot on its left & items greater than pivot on its right "
    swap_index = pivot_index  # Here we store the index instead of the value
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1  # swap_index+1 always points to the first item greater than pivot
            swap(my_list, i, swap_index)  # swap my_list[i], which is less than pivot, withthe first item greater than pivot
    swap(my_list, pivot_index, swap_index)
    return swap_index


my_list = [5, 3, 9, 1, 6, 7, 8, 0]
print(pivot(my_list, 0, 7))
print(my_list)