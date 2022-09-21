# Given an integer array, retrun all possible subsets. Note: [1, 2] ia the same subset as [2, 1]
# time complexity: O(n*2**n)
# backtracking
# https://www.youtube.com/watch?v=REOH22Xwdkk


def subsets(list):
    " Given an integer array, retrun all possible subsets. "
    result = []
    subset = []

    def dfs(index):
        "  "
        if index == len(list):  # When all elements have already been accsessed
            result.append(subset.copy())
            return
        # decision to include list[index]
        subset.append(list[index])
        dfs(index + 1)
        # decision to NOT include list[index]
        subset.pop()
        dfs(index + 1)
    dfs(0)
    return result
        

my_list = [1, 2, 3]
print(subsets(my_list))
