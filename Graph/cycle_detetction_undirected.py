# Cycle:
# For every visited vertex 'v', if there's an adjacent 'u' such that 'u' is already visited and not parent of 'v', then there's a cycle in teh graph

# Undirected graph


from collections import defaultdict


class Graph:

    def __init__(self, nodes: int):

        # The default dictionary would create an empty list as a default (value)
        # for the nonexistent keys.
        self.adjlist = defaultdict(list)
        self.nodes = nodes
        self.visited = [False] * nodes
        # parent stores the parent node of the visited node, this is used
        # for finding cycle in an un-directed graph.
        self.parent = [None] * nodes
        self.cycle_present = False

    def AddEdge(self, src: int, dst: int, bidirectional: bool):

        self.adjlist[src].append(dst)

        if bidirectional is True:
            self.adjlist[dst].append(src)

    # Function detects cycle in an undirected graph
    # using DFS technique at its core
    def DetectCycle(self, src: int):

        self.visited[src] = True

        for adj_node in self.adjlist[src]:
            if self.visited[adj_node] is False:
                self.parent[adj_node] = src
                self.DetectCycle(adj_node)
            elif self.parent[src] != adj_node:
                self.cycle_present = True
                return

    def CyclePresent(self):
        return self.cycle_present


def main():

    nodes = 7
    g1_undirected = Graph(nodes)

    # Undirected graph 1
    #           0
    #          / \
    #         1   2
    #            / \
    #           3   4
    #              / \
    #             5   6 */

    g1_undirected.AddEdge(0, 1, True)
    g1_undirected.AddEdge(0, 2, True)
    g1_undirected.AddEdge(2, 3, True)
    g1_undirected.AddEdge(2, 4, True)
    g1_undirected.AddEdge(4, 5, True)
    g1_undirected.AddEdge(4, 6, True)

    g1_undirected.DetectCycle(0)

    if g1_undirected.CyclePresent() is True:
        print("Cycle found in the undirected graph g1")
    else:
        print("Cycle not found in the undirected graph g1")

    nodes = 4

    g2_undirected = Graph(nodes)
    # Undirected graph 2
    #           0
    #          / \
    #         1   2
    #          \ /
    #           3
    g2_undirected.AddEdge(0, 1, True)
    g2_undirected.AddEdge(0, 2, True)
    g2_undirected.AddEdge(1, 3, True)
    g2_undirected.AddEdge(2, 3, True)

    g2_undirected.DetectCycle(0)

    if g2_undirected.CyclePresent() is True:
        print("Cycle found in the undirected graph g2")
    else:
        print("Cycle not found in the undirected graph g2")


if __name__ == "__main__":
    main()
