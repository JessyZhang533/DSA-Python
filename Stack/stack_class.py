# Analogy of stack: a can of temmis balls
# Here we build a stack using linked list

class Node:  # Same as in LinkedList
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        " Constructor "
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        " Print item in the stack one by one "
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):  # Equivalent to 'prepend'
        " Add an item to the (top of the) stack "
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):  # Equivalent to 'pop_first'
        " Remove an item from the (top of the) stack & return it "
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp


my_stack = Stack(4)
my_stack.push(1)
my_stack.pop()
my_stack.print_stack()
