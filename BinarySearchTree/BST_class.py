class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  # 'Less than' fork
        self.right = None  # 'Larger than' fork


class BinarySearchTree:
    def __init__(self):  # Here we do not pass argument 'value' so that an empty BST can be created
        self.root = None  # The uppermost node that has no parent node


my_tree = BinarySearchTree()
print(my_tree.root)

# Conclusion:
# 1. Use while loop instead of for loop when you don't know the exact number of iterations
