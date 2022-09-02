class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Arrow 1
        self.prev = None  # Arrow 2


class DoublyLinkedList:
    def __init__(self, value):
        " Constructor "
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        " Print all values one by one "
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next

    def append(self, value):
        " Add an item to the end of the list "
        new_node = Node(value)
        if self.head is None:  # Comparison to None should be "is None" instead of "== None"
            self.head = new_node
            self.tail = new_node
            self.length = 1
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True


my_doubly_linked_list = DoublyLinkedList(3)
my_doubly_linked_list.append(6)
my_doubly_linked_list.print_list()
