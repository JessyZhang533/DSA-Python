# A concept for DIRECTED graphs
# definition: https://www.youtube.com/watch?v=LvM8Qi-IvqE
# code reference: https://www.programiz.com/dsa/strongly-connected-components


# Kosaraju's algorithm to find strongly connected components in Python
# 1.Perform a depth first search on the whole graph.
# 2.Reverse the original graph.
# 3.Perform depth-first search on the reversed graph.

# Here vertices = consecutive integers

from collections import defaultdict


class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)  # https://docs.python.org/3/library/collections.html#collections.defaultdict

    # Add edge into the graph
    def add_edge(self, s, d):  # Edge points from s to d
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited_vertex):  # d is a vertex; Last argument is a list with values being booleans
        visited_vertex[d] = True
        print(d, end=' ')
        for i in self.graph[d]:
            if not visited_vertex[i]:  # If visited_vertex[i] == False
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):  # If a vertex leads to an already visited vertex, then push this vertex to the stack.
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    # transpose the matrix
    def transpose(self):  # Reverse the original graph
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # Print stongly connected components
    def print_scc(self):
        stack = []
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()  # reverse graph

        visited_vertex = [False] * (self.V)

        while stack:  # While the stack is not empty
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")


g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

print("Strongly Connected Components:")
g.print_scc()
