# Sort the list by breaking down, sorting smaller lists & combining
# 1. Break the list in half using recursion
# 2. Base case: len(smaller_list) == 1
# 3. use merge() to combine


def merge(list1, list2):
    " Combine two SORTED lists into one sorted list "
    combine = []  # Initialise the final sorted list
    i = 0
    j = 0  # Initialise indices
    while i < len(list1) and j < len(list2):  # Break the while loop when at least one of the lists are empty
        if list1[i] < list2[j]:  # Start from the smallest value of each list; append the smaller value in each loop
            combine.append(list1[i])
            i += 1
        else:
            combine.append(list2[j])
            j += 1

    while i < len(list1):  # If list 1 has remaining items
        combine.append(list1[i])
        i += 1
    while j < len(list2):  # If list 2 has remaining items
        combine.append(list2[j])
        j += 1

    return combine


def merge_sort(my_list):
    " Break the list in half; combine sorted lists "
    if len(my_list) == 1:  # base case
        return my_list
    mid = int(len(my_list)/2)  # 'int': if the value is 1.5, 'int' turns it into 1
    left_of_list = my_list[:mid]  # Slicing: up to and not including my_list[mid]
    right_of_list = my_list[mid:]  # Slicing: from and including my_list[mid]
    return merge(merge_sort(left_of_list), merge_sort(right_of_list))


print(merge([1, 4, 7, 8], [3, 5]))
print(merge_sort([9, 3, 5, 1, 6, 7, 8, 0]))
