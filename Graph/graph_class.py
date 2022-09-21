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

    def remove_edge(self, v1, v2):
        " Disconnect two vertices/Remove the edge between two vertices "
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:  # try...except ValueError pass: To fix the case where a vertex exists but is not connected, and an edge including this vertex is removed
                self.adj_list[v1].remove(v2)  # '.remove()'
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass  # Ignore the error and move on to return True
            return True
        return False  # At least one of the vertices is not in the graph

    def remove_vertex(self, vertex):
        " Remove the given vertex (& all associated edges) "
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)  # Remove all associated edges
            del self.adj_list[vertex]  # Delete the vertex as a key
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
