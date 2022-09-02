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
            return None  # function ends here
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

    def pop_first(self):
        " Remove the first item from the list & return it "
        if self.length == 0:
            return None  # function ends here
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None  # Cannot put this line in front of 'self.head = self.head.next',
# because if 'temp.next = None' comes first, then self.head.next will also be None. Therefore self.head.prev would be invalid because Nonetype has no attribute prev
        self.length -= 1
        return temp

    def get(self, index):
        " Return the node at the index "
        if index < 0 or index > (self.length - 1):
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):  # Iteration starts from the last item; decrement by one in each loop
                temp = temp.prev
        return temp.value


my_doubly_linked_list = DoublyLinkedList(3)
my_doubly_linked_list.append(6)
my_doubly_linked_list.pop()
my_doubly_linked_list.prepend(8)
my_doubly_linked_list.pop_first()
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
my_doubly_linked_list.append(6)
my_doubly_linked_list.append(7)
print(my_doubly_linked_list.get(3))
# my_doubly_linked_list.print_list()

# Conclusions:
# 1. If wanting to add an item to the list:
# (1) Consider 2 scenarios: self.length == 0; general
# (2) Always remember to create a new node
# 2. If wanting to remove an item from the list:
# (1) Consider 3 scenarios: self.length == 0; self.length == 1; general