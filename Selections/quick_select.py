# time complexity: average O(n)-->pivot always medium, worst O(n^2)-->pivot always the greatest/smallest value
# https://www.youtube.com/watch?v=XEmy13g1Qxc
# Find pivot and partition: same as quick sort
# An improvement from sort_then_select()

def quick_select(list, k):
    " Return the kth smallest eleent using divide and conquer "

    def partition(pivot_index, end_index):
        " Set pivot and divide a list into two parts "
        swap_index = pivot_index
        for i in range(pivot_index+1, end_index+1):
            if list[i] < list[pivot_index]:
                swap_index += 1
                list[i], list[swap_index] = list[swap_index], list[i]
        list[pivot_index], list[swap_index] = list[swap_index], list[pivot_index]
        if swap_index < k:
            return partition(swap_index+1, end_index)
        elif swap_index > k:
            return partition(0, swap_index-1)
        else:
            return list[swap_index]

    return partition(0, len(list) - 1)


my_list = [4, 0, 9, 5, 7, 2]
print(quick_select(my_list, 3))  # Return the third smallest, should be 5
