# New nodes need to be created in every method of the linked list class,
# so here we create a class that's particularly for creating new nodes
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Below is the linked list class
class LinkedList:
    def __init__(self, value):
        " Constructor "
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self, value):
        " Print the items in the linked list one by one "
        temp = self.head
        while temp is not None:  # when the list is not none
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
my_linked_list.print_list(4)
