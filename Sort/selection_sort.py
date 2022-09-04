def selection_sort(my_list):
    " Sort the list by finding out the index of the smallest value, second smallest value, etc. "
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[min_index] > my_list[j]:
                min_index = j
        temp = my_list[min_index]
        my_list[min_index] = my_list[i]
        my_list[i] = temp
    return my_list


my_list = [19, 8, 10, 7, 1, 2]
print(selection_sort(my_list))

# Figured this out entirely by myself yayyyyy
# t.c.=O(n^2)
# s.c.=O(1)
