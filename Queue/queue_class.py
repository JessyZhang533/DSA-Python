# Analogy of a queue: a real queue
# Here we build a queue using linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        " Constructor "
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        " Print items in a queue one by one "
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next


my_queue = Queue(2)
my_queue.print_queue()
