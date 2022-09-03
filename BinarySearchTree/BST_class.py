class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  # 'Less than' fork
        self.right = None  # 'Larger than' fork


class BinarySearchTree:
    def __init__(self):  # Here we do not pass argument 'value' so that an empty BST can be created
        " Constructor "
        self.root = None  # The uppermost node that has no parent node

    def insert(self, value):
        " Insert an item into the tree "
        new_node = Node(value)
        if self.root is None:  # Edge case 1: original tree is empty
            self.root = new_node
            return True  # To end the function
        temp = self.root
        while True:
            if new_node.value == temp.value:  # Edge case 2: new value already existing
                return False
            if new_node.value < temp.value:  # Go left
                if temp.left is None:
                    temp.left = new_node
                    return True  # To end the function
                temp = temp.left
            else:  # Go right
                if temp.right is None:
                    temp.right = new_node
                    return True  # To end the function
                temp = temp.right


my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
print(my_tree.root.left.value)  # Should be 1

# Conclusion:
# 1. Use while loop instead of for loop when you don't know the exact number of iterations
# 2. If the function should stop executing under some condition, use 'return ...' instead of an if statement
