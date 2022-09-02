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
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next


my_doubly_linked_list = DoublyLinkedList(3)
my_doubly_linked_list.print_list()
