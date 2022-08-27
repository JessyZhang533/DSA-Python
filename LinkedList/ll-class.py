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
        while temp is not None:  # Iterate
            print(temp.value)
            temp = temp.next

    def append(self, value):
        " Append an item to the end of the linked list "
        new_node = Node(value)
        if self.head is None:  # when the list is None
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True  # Will be explained later

    def pop(self):
        " Remove an item from the end of the linked list and then return this item"
        if self.length == 0:  # Edge case 1: If the list is None
            return None
        temp = self.head
        pre = self.head
        while(temp.next):  # Equivalent to: while temp.next is True/not None
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None  # remove the last item
        self.length -= 1
        if self.length == 0:  # Edge case 2: If the list has length 1
            self.head = None
            self.tail = None
        return temp.value  # return the entire (last) node. If want to return value, use: 'return temp.value'


my_linked_list = LinkedList(4)
# print(my_linked_list.head.value)
my_linked_list.append(1)
# my_linked_list.print_list()
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
