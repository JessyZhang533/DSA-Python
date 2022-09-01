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
        while(temp):  # Iterate; Equivalent to: while temp is True/not None
            print(temp.value)
            temp = temp.next

    def append(self, value):
        " Add an item to the end of the linked list "
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
        " Remove an item from the end of the linked list and then return this item "
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
        return temp.value  # If want to return value, use: 'return temp.value'; if want to return the entire node, use: 'return temp'

    def prepend(self, value):
        " Add an item to the start of the list "
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1  # Always remember to update length since it is too an attribute
        return True  # Will be explained later

    def pop_first(self):
        " Remove an item from the start of the linked list and then return this item "
        if self.length == 0:  # Edge case 1: If the list is None
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None  # Remove the first item
        self.length -= 1
        if self.length == 0:  # Edge case 2: If the list has length 1
            self.tail = None
        return temp.value  # If want to return value, use: 'return temp.value'; if want to return the entire node, use: 'return temp'

    def get(self, index):
        " Return the node at the 'index' "
        if index < 0 or index > (self.length - 1):
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp  # If want to return value, use: 'return temp.value'; if want to return the entire node, use: 'return temp'

    def set_value(self, index, value):
        " Change the value of a node at a certain 'index' "
        temp = self.get(index)  # Use the method we created earlier. Note that if we want this to work, 'get' should return the node(ie.temp) instead of just the value(ie.temp.value)
        if temp:  # If temp is True/not None
            temp.value = value  # assign value directly
            return True
        return False

    def insert(self, index, value):
        " Insert a value in the list at the position 'index' "
        if index < 0 or index > (self.length - 1):
            return False
        if index == 0:  # Reuse function
            return self.prepend(value)
        if index == self.length:  # Reuse function
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next  # So that we don't have to create another pointer
        temp.next = new_node
        self.length += 1  # Always remember to update the length!!!
        return True


my_linked_list = LinkedList(4)
# print(my_linked_list.head.value)
my_linked_list.prepend(1)
my_linked_list.append(7)
print(my_linked_list.get(1))  # Note that we can't display the value if not having the print statement
my_linked_list.set_value(0, 5)
my_linked_list.insert(1, 9)
my_linked_list.print_list()
