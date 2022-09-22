# Print/Visit every vertices of the graph; traverse the graph by going to the end of one path at a time
# In this algorithm, we will be using the concept of 'Stack'
# t.c.: O(V+E)
# s.c.: O(V)
# Here we implement the graph using adjacency list (a dic)
# https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=1348s


nodes_visited = []  # keep track of what nodes are visited


def dfs_graph(graph, node):
    " Print/Visit every vertices of the graph; traverse the graph by going to the end of one path at a time "
    if node not in nodes_visited:
        print(node)
        nodes_visited.append(node)
        for adj_node in graph[node]:
            dfs_graph(graph, adj_node)


my_graph = {
  '5': ['3', '7'],
  '3': ['2', '4'],
  '7': ['8'],
  '2': [],
  '4': ['8'],
  '8': []
}  # This is a Directed Graph
dfs_graph(my_graph, '5')
