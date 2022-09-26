# Here we use adjacent list (a dictionary) to create a graph
# 1. Directed Graph & Undirected Graph (edges have arrows or not)
# Undirected: if we have A:['B'], then we must have the inverse path B:['A']
# https://www.youtube.com/watch?v=amaH38_mXK4

class Graph:  # This class is Undirected Graph
    def __init__(self):
        " Constructor "
        self.adj_list = {}

    def add_vertex(self, vertex):
        " Add an vertex to the graph "
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def print_graph(self):
        " Print the adjacent list (dictionary) without '{}' "
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")

    def add_edge(self, v1, v2):
        " Connect two vertices with an edge "
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)  # This line is for undirected graph. directed graph do not need this line
            return True
        return False

    def remove_edge(self, v1, v2):
        " Disconnect two vertices/Remove the edge between two vertices "
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)  # This line is for undirected graph. directed graph do not need this line
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        " Remove the given vertex (& all associated edges) "
        if vertex in self.adj_list:
            for other_vertex in self.adj_list[vertex]:  # !!! Only iterate through vertices connected with the given vertex
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('C', 'B')
my_graph.remove_vertex('C')
my_graph.print_graph()

# Conclusions:
# 1. Two methods for the list: '.append()', '.remove()'
# 2. Delete an object: 'del' https://www.programiz.com/python-programming/del
