def insertion_sort_1(my_list):  # my version
    " Sort the list by: starting from the second item, put it to the left most place (left = small)  "
    for i in range(1, len(my_list)):
        temp = my_list[i]
        for j in range(i-1, -1, -1):  # cannot reach -1, can only decrease to 0
            if temp < my_list[j]:
                my_list[j + 1] = my_list[j]
                my_list[j] = temp
    return my_list


def insertion_sort_2(my_list):  # udemy version
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


my_list = [19, 8, 10, 7, 1, 2]
print(insertion_sort_1(my_list))
print(insertion_sort_2(my_list))

