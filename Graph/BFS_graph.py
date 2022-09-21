# Print/Visit every vertices of the graph; traverse the graph by exploring every other vertices connected to one vertex
# In this algorithm, we will be using the concept of 'Queue'
# t.c.: O(V+E)
# s.c.: O(V)
# Here we implement the graph using adjacent list (a dic)


def bfs_graph(graph, node):
    " Print/Visit every vertices of the graph; traverse the graph by exploring every other vertices connected to one vertex "
    queue = []
    nodes_visited = []

    queue.append(node)
    nodes_visited.append(node)
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        for adj_node in graph[m]:
            if adj_node not in nodes_visited:
                queue.append(adj_node)
                nodes_visited.append(adj_node)


my_graph = {
  '5': ['3', '7'],
  '3': ['2', '4'],
  '7': ['8'],
  '2': [],
  '4': ['8'],
  '8': []
}  # This is a Directed Graph
bfs_graph(my_graph, '5')
