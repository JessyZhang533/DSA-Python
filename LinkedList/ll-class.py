# New nodes need to be created in every method of the linked list class,
# so here we create a class that's particularly for creating new nodes
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Below is the linked list class
class LinkedList:

    # constructor
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
