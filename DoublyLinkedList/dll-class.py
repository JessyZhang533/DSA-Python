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

    def pop(self):
        " Remove an item from the end of the list & return it "
        if self.head is None:  # Edge case 1: list is none
            return None
        temp = self.tail
        if self.length == 1:  # Edge case 2: (original)list has length of 1. We consider this case because need to point self.head to None.
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None  # Note: Nonetype object has no attribute 'next'. This is why we need  to separate Edge case 2 in an if statement
            temp.prev = None
        self.length -= 1
        return temp  # Node: temp; Value: temp.value
        # If with else: some do this, some do that;
        # If without else: all do this, some do additional stuff in the if statement

    def prepend(self, value):
        " Add an item to the start of the list "
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
        return True


my_doubly_linked_list = DoublyLinkedList(3)
my_doubly_linked_list.append(6)
my_doubly_linked_list.pop()
my_doubly_linked_list.prepend(8)
my_doubly_linked_list.print_list()
