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


    def print_list(self):
        " Print the items in the linked list one by one "
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


    def append(self, value):
        " Add an item to the end of the linked list "

    def pop(self):
        " Remove an item from the end of the linked list and then return this item "


    def prepend(self, value):
        " Add an item to the start of the list "



    def pop_first(self):
        " Remove an item from the start of the linked list and then return this item "


    def get(self, index):
        " Return the node at the 'index' "


    def set_value(self, index, value):
        " Change the value of a node at a certain 'index' "


    def insert(self, index, value):
        " Insert a value in the list at the position 'index' "


    def remove(self, index):
        " Remove the item at the index "


    def reverse(self):
        " Reverse the sequence of the list "



my_linked_list = LinkedList(4)
# print(my_linked_list.head.value)
my_linked_list.prepend(1)
my_linked_list.append(7)
print(my_linked_list.get(1))  # Note that we can't display the value if not having the print statement
my_linked_list.set_value(0, 5)
my_linked_list.insert(1, 9)
my_linked_list.remove(3)
my_linked_list.reverse()
my_linked_list.print_list()
