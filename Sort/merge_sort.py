# Sort the list by breaking down, sorting smaller lists & combining


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


print(merge([1, 4, 7, 8], [3, 5]))
