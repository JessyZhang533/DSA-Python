# Input number of vertices and all edges (stored as a list of lists), return number of connected components/chunks
# A concept for UNDIRECTED graphs
# https://www.youtube.com/watch?v=Y29g_m96iaI

def count_components(num_of_vtx, edges):
    " Input number of vertices and all edges (stored as a list of lists), return number of connected components/chunks "
    if num_of_vtx == 1:  # Edge case: graph has only one vertex & no edges
        return 1
    components = 0  # Initialise number of components
    graph = {node: [] for node in range(num_of_vtx)}  # Initialise the graph using adjacency list. Vertices are consecutive integers
    for node1, node2 in edges:  # Create the graph
        graph[node1].append(node2)
        graph[node2].append(node1)  # Undirected graph

    visited = []  # Visited, appended

    def dfs(node):  # Input a node/vertex, and visit all nodes/vertices in the same component/chunk with it
        " Perform depth first search "
        for adj_node in graph[node]:
            if adj_node not in visited:
                visited.append(adj_node)
                dfs(adj_node)

    for node in graph:  # Note: when program executes, it would skip the dfs() function and go straight to this block of codes
        if node in visited:
            continue
        else:
            visited.append(node)  # DONOT forget
            components += 1
            dfs(node)

    return components


print(count_components(5, [[0, 1], [1, 2], [3, 4]]))
