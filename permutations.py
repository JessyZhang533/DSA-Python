# Return all permutations of a list.
# 1. Make a copy of a list:
# (1) Shallow copy: the copied list is not the same thing as the original one, but their elements are the exact same things. eg..copy(), [:]
# (2) Deep copy: the copied list is not the same thing as the original one, elements are not the same thing
# https://stackoverflow.com/questions/17246693/what-is-the-difference-between-shallow-copy-deepcopy-and-normal-assignment-oper
# 2. Two main steps of the permutation algorithm: first pop, then append back
# 3. Add multiple items to a list: .extend()
def permutation(list):
    " Return all permutations of a list "
    result = []
    # base case
    if len(list) == 1:
        return [list[:]]
    for _ in range(len(list)):
        n = list.pop(0)  # Here the poped element, n, used to be the first of the list
        perms = permutation(list)  # here the 'perms' will contain all permutations of the popped/updated list that we input into 'permutation'
        for perm in perms:
            perm.append(n)
        result.extend(perms)  # 'result' of the first (bottom) call stack of 'permutation' function will always be updated with more and more final permutations
        list.append(n)  # Now we add n back, it has become the last of the list
    return result


my_list = [1, 2, 3]
print(permutation(my_list))
