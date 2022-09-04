# Here we use adjacent list (a dictionary) to create a graph

class Graph:
    def __init__(self):
        " Constructor "
        self.adj_list = {}

    def add_vertex(self, vertex):
        " Add an vertex to the graph "
        if vertex not in self.adj_list.keys():  # Don't want duplicates; note 'not in', '.keys()'
            self.adj_list[vertex] = []  # An enpty list used to contain adjacent vertices
            return True  # !!!
        return False

    def print_graph(self):
        " Print the adjacent list (dictionary) without '{}' "
        for vertex in self.adj_list:
            print(vertex, ": ", self.adj_list[vertex])


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.print_graph()
