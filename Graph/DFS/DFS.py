# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
# Python program to print DFS traversal from a
# given given graph
from collections import defaultdict  # if a key that is not in the dict is attempt

# This class represents a directed graph
# adjacency list representation - a dictionary of sets
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        # self.graph = defaultdict(list)
        self.graph = defaultdict(set)
        self.visited = set()
        # function to add an edge to graph

    # O(1)
    def addEdge(self, u, v):
        self.graph[u].add(v)


    def dfsRecursive(self, v):

        self.visited.add(v)

        print( v,)

        for i in self.graph[v]:   # Recur for all the vertices adjacent to this vertex
            if i not in self.visited:
                self.dfsRecursive(i)


    def dfsIterative(self, v):
        stack = [v]
        while stack:
            vertex = stack.pop()
            if vertex not in self.visited:
                self.visited.add(vertex)
                print(vertex)
                stack.extend(self.graph[vertex] - self.visited) # add unvisited neighbors (set subtraction)
        return self.visited

# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
# g.dfsRecursive(2)
print(g.dfsIterative(2))
# This code is contributed by Neelam Yadav