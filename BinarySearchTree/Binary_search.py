def BS_iterative(list, val):
    " Return the index of val in the given SORTED list; use while loop "
    lower, upper = 0, len(list) - 1
    if val < list[lower] or val > list[upper]:
        return None
    while True:
        mid = (lower + upper) // 2
        if val < list[mid]:
            upper = mid - 1
        elif val > list[mid]:
            lower = mid + 1
        else:
            return mid
        if lower > upper:
            return None


def BS_recursive(list, val):
    " Return the index of val in the given SORTED list; use recursion "
    lower, upper = 0, len(list) - 1
    if val < list[lower] or val > list[upper]:
        return None

    def BS_help(lower, upper):
        if lower > upper:
            return None
        mid = (lower + upper) // 2
        if val < list[mid]:
            return BS_help(lower, mid - 1)
        if val > list[mid]:
            return BS_help(mid + 1, upper)
        return mid

    return BS_help(lower, upper)  # !!! PLEASE DONOT FORGET 'RETURN', otherwise it would return None no matter what


my_list = [1, 4, 5, 12, 35, 89]
print(BS_iterative(my_list, 12))
print(BS_recursive(my_list, 12))


# Solution online
def binary_search_recursive(arr, elem, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return False

    mid = (start + end) // 2
    if elem == arr[mid]:
        return mid
    if elem < arr[mid]:
        return binary_search_recursive(arr, elem, start, mid-1)
    # elem > arr[mid]
    return binary_search_recursive(arr, elem, mid+1, end)


print(binary_search_recursive(my_list, 12, 0))
