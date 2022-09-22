# Cycle:
# For every visited vertex 'v', if there's an adjacent 'u' such that 'u' is already visited and not parent of 'v', then there's a cycle in teh graph

# Directed graph
# Here we implement the graph using adjacent list (a dic)


from collections import defaultdict


class Graph:

    def __init__(self, nodes: int):
        # The default dictionary would create an empty list as a default (value)
        # for the nonexistent keys.
        self.adjlist = defaultdict(list)
        self.nodes = nodes
        self.visited = [False] * nodes
        # inpath stores the visited nodes in the traversal path
        # for finding cycle in a directed graph.
        self.inpath = [False] * nodes
        self.cycle_present = False

    def AddEdge(self, src: int, dst: int, bidirectional: bool):

        self.adjlist[src].append(dst)

        if bidirectional:  # Check if the edge is undirected (bidirectional)
            self.adjlist[dst].append(src)

    # Function detects cycle in a directed graph using
    # DFS technique at its core.
    def DetectCycle(self, src: int):

        self.visited[src] = True

        # Set the flag for the vertex visited in traversal path
        self.inpath[src] = True

        for adj_node in self.adjlist[src]:

            if self.inpath[adj_node] is True:
                self.cycle_present = True
                return
            elif self.visited[adj_node] is False:
                self.DetectCycle(adj_node)

        # Before we backtrack unset the flag for the src vertex as it
        # might be in the next traversal path
        self.inpath[src] = False

    # Mark nodes unvisited for the next traversal
    def MarkUnvisited(self):
        self.visited = [False] * self.nodes

    def CyclePresent(self):
        return self.cycle_present


def main():

    nodes = 7
    g1_directed = Graph(nodes)

    #  Graph 1
    #  6-----------
    #  ^          |
    #  |          |
    #  4<------5<--
    #  ^       ^
    #  |       |
    #  1<------3
    #  ^       ^
    #  |       |
    #  0 ----->2

    # Add edges to the directed graph
    g1_directed.AddEdge(0, 1, False)
    g1_directed.AddEdge(0, 2, False)
    g1_directed.AddEdge(1, 4, False)
    g1_directed.AddEdge(2, 3, False)
    g1_directed.AddEdge(3, 1, False)
    g1_directed.AddEdge(3, 5, False)
    g1_directed.AddEdge(4, 6, False)
    g1_directed.AddEdge(5, 4, False)
    g1_directed.AddEdge(6, 5, False)

    g1_directed.DetectCycle(0)

    if g1_directed.CyclePresent() is True:
        print("Cycle found in the directed graph g1")
    else:
        print("Cycle not found in the directed graph g1")

    # Graph 2
    # 4-
    # ^ \
    # |  \
    # 3   \
    # ^    \
    # |     \
    # 2      \
    # ^       \
    # |        \
    # 0--->1<---

    nodes = 5
    g2_directed = Graph(nodes)

    g2_directed.AddEdge(0, 1, False)
    g2_directed.AddEdge(0, 2, False)
    g2_directed.AddEdge(2, 3, False)
    g2_directed.AddEdge(3, 4, False)
    g2_directed.AddEdge(4, 1, False)

    g2_directed.DetectCycle(0)

    if g2_directed.CyclePresent() is True:
        print("Cycle found in the directed graph g2")
    else:
        print("Cycle not found in the directed graph g2")


if __name__ == "__main__":
    main()
