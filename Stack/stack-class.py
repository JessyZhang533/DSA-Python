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
        self.top = new_node  # Equivalent to 'self.head'
        # self.bottom = None  # Equivalent to 'self.tail', but we don't need this in stack
        self.height = 1  # Equivalent to 'self.length'

    def print_stack(self):
        " Print item in the stack one by one "
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next


my_stack = Stack(4)
my_stack.print_stack()
