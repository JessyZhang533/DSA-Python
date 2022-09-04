# Interview Question: Write a function that checks if two lists have at least one item in common
# Method 2 using a dictionary is recommended

# Method 1
def item_in_common_1(list1, list2):
    " Use nested for loops; time complexity O(n^2) "
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


# Method 2
def item_in_common_2(list1, list2):
    " Use dictionaries; time complexity O(n) "
    my_dic = {}
    for i in list1:  # items in list1 as keys in my_dic
        my_dic[i] = True
    for j in list2:  # look up the keys
        if j in my_dic:
            return True
    return False


a = [1, 2, 3]
b = [4, 8, 7]
print(item_in_common_1(a, b))
print(item_in_common_2(a, b))
