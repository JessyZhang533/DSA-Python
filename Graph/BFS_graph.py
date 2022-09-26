# Print/Visit every vertices of the graph; traverse the graph by exploring every other vertices connected to one vertex
# In this algorithm, we will be using the concept of 'Queue'
# t.c.: O(V+E)
# s.c.: O(V)
# Here we implement the graph using adjacency list (a dic)
# https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=1348s


def BFS_graph(graph, vertex):
    " Start from the given vertex, traverse the graph using breadth first search "
    queue = []
    result_list = []
    queue.append(vertex)
    while queue:
        current_vertex = queue.pop(0)
        result_list.append(current_vertex)  # These above 6 lines are the same as in BST
        for other_vertex in graph[current_vertex]:
            if other_vertex not in result_list and other_vertex not in queue:  # !!! "not in result_list and not in queue"
                queue.append(other_vertex)
    return result_list


my_graph = {
  '5': ['3', '7'],
  '3': ['2', '4'],
  '7': ['8'],
  '2': [],
  '4': ['8'],
  '8': []
}  # This is a Directed Graph
print(BFS_graph(my_graph, '5'))
