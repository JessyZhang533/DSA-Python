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
        new_node = Node(value)
        if self.length == 0:  # Edge case 1
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = self.tail.next
        self.length += 1
        return True  # Used in insert()

    def pop(self):
        " Remove an item from the end of the linked list and then return this item "
        if self.head is None:  # Edge case 1
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:  # Edge case 2
            self.head = None
            self.tail = None  # !!!
        return temp  # temp Or temp.value

    def prepend(self, value):
        " Add an item to the start of the list "
        new_node = Node(value)
        if self.head is None:  # Edge case 1
            self.head = new_node
            self.tail = new_node
        else:  # !!! We have no 'return' statement in the 'if' statement; so we need an else' to separate the code
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True  # Used in insert()

    def pop_first(self):
        " Remove an item from the start of the linked list and then return this item "
        if self.head is None:  # Edge case 1
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:  # Edge case 2
            self.tail = None
        return temp   # temp Or temp.value

    def get(self, index):
        " Return the node at the 'index' "
        if index < 0 or index > (self.length - 1):
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp  # Will be used in 'insert' and 'remove', so must return a node instead of a value

    def set_value(self, index, value):  # !!! No need to create a new node
        " Change the value of a node at a certain 'index' "
        temp = self.get(index)
        if temp:
            temp.value = value  # Set value directly
            return True
        return False

    def insert(self, index, value):
        " Insert a value in the list at the position 'index' "
        if index < 0 or index > (self.length - 1):
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        " Remove the item at the index "  # SEE REQUIREMENT FIRST. No returning anything here
        if index < 0 or index > (self.length - 1):
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = self.get(index)
        pre.next = temp.next
        temp.next = None

    def reverse(self):  # !!!
        " Reverse the sequence of the list "
        temp = self.head
        self.head = self.tail
        self.tail = temp  # This line and above: reverse pointers head and tail only
        before = None  # This line and below: reverse every arrow
        for _ in range(self.length):  # 3 pointers moving along: before, temp, after
            after = temp.next
            temp.next = before  # REVERSE
            before = temp  # Move pointer
            temp = after  # Move pointer


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
