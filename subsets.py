# Given an integer array, retrun all possible subsets. Note: [1, 2] ia the same subset as [2, 1]; NO duplicate subsets
# time complexity: O(n*2**n)
# backtracking
# https://www.youtube.com/watch?v=REOH22Xwdkk
# https://www.youtube.com/watch?v=Vn2v6ajA7U0


def subsets_no_duplicate(list):
    " Given an integer array, retrun all possible subsets. Argument has no duplicate values. "
    result = []
    subset = []

    def dfs(index):
        " Take an index as argument; two branches, one to include list[index] and the other not to "
        if index == len(list):  # Exit when all elements have already been accsessed
            result.append(subset.copy())
            return
        # decision to include list[index]--branch 1
        subset.append(list[index])
        dfs(index + 1)  # Recursion
        # decision to NOT include list[index]--branch 2
        subset.pop()  # .pop() default argument is -1
        dfs(index + 1)
    dfs(0)
    return result


my_list = [1, 2, 3]
print(subsets_no_duplicate(my_list))


def subsets_has_duplicate(list):
    " Given an integer array, retrun all possible subsets. Argument has duplicate values. "
    " Given an integer array, retrun all possible subsets. Argument has no duplicate values. "
    result = []
    list.sort()

    def backtrack(index, subset):
        " Take an index as argument; two branches, one to include list[index] and the other not to "
        if index == len(list):  # Exit when all elements have already been accsessed
            result.append(subset.copy())
            return
        # decision to include list[index]--branch 1
        subset.append(list[index])
        backtrack(index + 1, subset)  # Recursion
        # decision to NOT include list[index]--branch 2
        subset.pop()
        while (index + 1) < len(list) and list[index] == list[index+1]:
            index += 1
        backtrack(index + 1, subset)
    backtrack(0, [])
    return result


my_list_has_duplicate = [1, 2, 2, 3]
print(subsets_has_duplicate(my_list_has_duplicate))
