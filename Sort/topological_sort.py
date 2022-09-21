# For a Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge (u, v), vertex u comes before v in the ordering
# Time complexity: O(V + E) -- V: number of vertices, E: number of edges
# https://www.youtube.com/watch?v=Q9PIxaNGnig


def toppological_sort(graph, num_of_vtx):
    degree = [0]*num_of_vtx
    for node in graph:
        for adj_node in graph[node]:
            degree[adj_node] += 1  # The number in this list indicates how many nodes are pointing at a certain node
    bfs = [i for i in range(num_of_vtx) if degree[i] == 0]  # These are the nodes that have no other nodes pointing at
    for node in bfs:
        for adj_node in graph[node]:
            degree[adj_node] -= 1
            if degree[adj_node] == 0:  # If a node has no unvisited neighbour
                bfs.append(adj_node)
    return bfs
    