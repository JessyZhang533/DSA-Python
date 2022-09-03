# Analogy of a queue: a real queue
# Here we build a queue using linked list

class Node:  # Same as Linked List
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        " Constructor "
        new_node = Node(value)
        self.first = new_node  # Equivalent to 'self.head'
        self.last = new_node  # Equivalent to 'self.tail'
        self.length = 1

    def print_queue(self):
        " Print items in a queue one by one "
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):  # Equivalent to 'append'
        " Add an item to (the end og the) queue "
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
            self.length = 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1


my_queue = Queue(2)
my_queue.enqueue(4)
my_queue.print_queue()
