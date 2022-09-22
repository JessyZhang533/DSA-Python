# Print/Visit every vertices of the graph; traverse the graph by exploring every other vertices connected to one vertex
# In this algorithm, we will be using the concept of 'Queue'
# t.c.: O(V+E)
# s.c.: O(V)
# Here we implement the graph using adjacency list (a dic)
# https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=1348s


def bfs_graph(graph, node):
    " Print/Visit every vertices of the graph; traverse the graph by exploring every other vertices connected to one vertex "
    queue = []
    nodes_visited = []

    queue.append(node)
    nodes_visited.append(node)
    while queue:
        m = queue.pop(0)  # concept of queue: first out
        print(m, end=" ")  # end=" ": each printed item is separated with a blank
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
