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

    def add_edge(self, v1, v2):
        " Connect two vertices with an edge "
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():  # Check if the vertex id in the graph
            self.adj_list[v1].append(v2)  # '.append()'
            self.adj_list[v2].append(v1)
            return True
        return False  # At least one of the vertices is not in the graph


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_edge('A', 'B')
my_graph.print_graph()
