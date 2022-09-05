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
                    return True  # To end the method
                temp = temp.left
            else:  # Go right
                if temp.right is None:
                    temp.right = new_node
                    return True  # To end the method
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

    def BFS(self):
        " Breadth First Search: traverse nodes row by row, store their values in a list & return the list "
        current_node = self.root
        queue = []
        result_list = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)  # Clear the items in 'queue' one by one
            result_list.append(current_node.value)  # We need the VALUE not the nodes in the result
            if current_node.left:  # Add nodes of the next row to 'queue'
                queue.append(current_node.left)
            if current_node.right:  # Add nodes of the next row to 'queue'
                queue.append(current_node.right)
        return result_list  # The structure of this list is like rows of the original tree stacked together

    def dfs_pre_order(self):
        " Traverse nodes downwards to the bottom from left to right, store their values in a list & return the list "
        result_list = []

        def traverse(current_node):  # A function inside a method
            " A recursive function governing the rules of traversing "
            result_list.append(current_node.value)
            if current_node.left is not None:  # This goes all the way down to the left
                traverse(current_node.left)
            if current_node.right is not None:  # This goes all the way down to the right
                traverse(current_node.right)

        traverse(self.root)
        return result_list

    def dfs_post_order(self):
        " Traverse down to bottom without storing, store values of nodes (in a list) from bottom to top, left to right & return the list  "
        result_list = []

        def traverse(current_node):
            " A recursive function governing the rules of traversing "
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            result_list.append(current_node.value)

        traverse(self.root)
        return result_list

    def dfs_in_order(self):
        " Store values of nodes in a list and return it. The final list looks like the original tree being squashed "
        result_list = []

        def traverse(current_node):
            " A recursive function governing the rules of traversing "
            if current_node.left is not None:
                traverse(current_node.left)
            result_list.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return result_list


my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
my_tree.insert(-89)
my_tree.insert(-8)
my_tree.insert(7)
my_tree.insert(36)
# print(my_tree.root.left.value)  # Should be 1
# print(my_tree.contain(4))  # Returns nothing without 'print'!
# print(my_tree.min_value_node(my_tree.root))
print(my_tree.BFS())
print(my_tree.dfs_pre_order())
print(my_tree.dfs_post_order())
print(my_tree.dfs_in_order())

# Conclusion:
# 1. Use while loop instead of for loop when you don't know the exact number of iterations
# 2. If the function/method should stop executing under some condition, use 'return ...' instead of an if statement
# 3. If there's only 'return...'as the output of a function/method, we need to use 'print' to visualise the output
# 4. Pop method for lists: '.pop(index)'
# 5. For BFS & DFS methods, remember to use 'call stack' to improve understanding. An input is removed from the call stack once it has gone thru every line of the method/function
