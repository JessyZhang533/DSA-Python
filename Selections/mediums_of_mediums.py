# time complexity: O(n)
# Median of medians can be used as a pivot strategy in quick_select, yielding an optimal algorithm.
# Procedure:
# 1.Select a pivot:
# (1) Split a list of unordered items into groups of five elements each.
# (2) Sort and find the median of all the groups.
# (3) Repeat step (1) and step (2) recursively to obtain the true median of the list.
# 2. Use the true median to partition the list of unordered items.
# 3. Recurse into the part of the partitioned list that may contain the ith-smallest element.
# Reference: https://brilliant.org/wiki/median-finding-algorithm/


def median_of_medians_pivot(my_list):
    " Return the kth smallest eleent using divide and conquer & a pivot strategy "
    sublists = [my_list[j:j+5] for j in range(0, len(my_list), 5)]  # list comprehension
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians)//2]
        return pivot
    else:
        median_of_medians_pivot(medians, len(medians)//2)


def quick_select(list, k):
    " Return the kth smallest element using divide and conquer "

    def partition(remaining_list, start_index, end_index):
        " Set pivot and divide a list into two parts "
        pivot = median_of_medians_pivot(remaining_list)
        print(pivot)
        swap_index = start_index
        for i in range(start_index, end_index+1):
            if list[i] < pivot:
                list[i], list[swap_index] = list[swap_index], list[i]
                swap_index += 1
        if swap_index < k:
            return partition(list[swap_index+1:], swap_index+1, end_index)
        elif swap_index > k:
            return partition(list[:swap_index], 0, swap_index)
        else:
            return list[swap_index]

    return partition(list, 0, len(list) - 1)


my_list = [4, 0, 9, 5, 7, 2]
print(quick_select(my_list, 3))
