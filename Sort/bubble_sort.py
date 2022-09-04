def bubble_sort_1(my_list):  # Cambridge notebook version
    " Sort the list by bubbling up the largest item in each loop "
    N = len(my_list)
    while N > 0:
        for i in range(N - 1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        N = N - 1
    return my_list


def bubble_sort_2(my_list):  # New version using decreasing for loop & pointer
    for i in range(len(my_list) - 1, 0, -1):  # largest, second largest, third largest, ...
        for j in range(i):  # The process of bubbling up the first/second/third/... largest
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list


my_list = [19, 8, 10, 7, 1, 2]
print(bubble_sort_1(my_list))
print(bubble_sort_2(my_list))
