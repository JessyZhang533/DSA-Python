# Print/Visit every vertices of the graph; traverse the graph by going to the end of one path at a time
# In this algorithm, we will be using the concept of 'Stack'
# t.c.: O(V+E)
# s.c.: O(V)
# Here we implement the graph using adjacency list (a dic)
# https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=1348s


def DFS_graph(self, vertex):
    " Print/Visit every vertices of the graph; traverse the graph by going to the end of one path at a time "
    result_list = []

    def traverse(current_vertex):
        " A function governing the rules of traversal "
        if current_vertex not in result_list:
            result_list.append(current_vertex)
        for other_vertex in self[current_vertex]:
            traverse(other_vertex)

    traverse(vertex)
    return result_list


my_graph = {
  '5': ['3', '7'],
  '3': ['2', '4'],
  '7': ['8'],
  '2': [],
  '4': ['8'],
  '8': []
}  # This is a Directed Graph
print(DFS_graph(my_graph, '5'))
