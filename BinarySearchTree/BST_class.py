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

    def contain(self, value):  # Don't need to separate any edge case
        " See if a value exist in the tree "
        temp = self.root
        while temp:
            if value == temp.value:
                return True  # The value IS in the tree
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False  # If iterates until temp is None, return False

    def min_value_node(self, current_node):
        " Find & return the child node of minimum value starting from a random node "
        while current_node.left:
            current_node = current_node.left
        return current_node  # Use current_node.value if wants to return value of node


my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
print(my_tree.root.left.value)  # Should be 1
print(my_tree.contain(4))  # Returns nothing without 'print'!
print(my_tree.min_value_node(my_tree.root))

# Conclusion:
# 1. Use while loop instead of for loop when you don't know the exact number of iterations
# 2. If the function should stop executing under some condition, use 'return ...' instead of an if statement
# 3. If there's only 'return...'as the output of a function, we need to use 'print' to visualise the output
