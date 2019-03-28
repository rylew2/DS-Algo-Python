# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

from collections import defaultdict

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

        print( v, end=' ')

        for i in self.graph[v]:   # Recur for all the vertices adjacent to this vertex
            if i not in self.visited:
                self.dfsRecursive(i)


    def dfsIterative(self, v):
        stack = [v]
        while stack:
            vertex = stack.pop()
            if vertex not in self.visited:
                self.visited.add(vertex)
                print(vertex, end=' ')
                stack.extend(self.graph[vertex] - self.visited) # add unvisited neighbors (set subtraction)
        return self.visited


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print('Recursive: ', end=' ')
g.dfsRecursive(2)

print()
print('============================')


g2 = Graph()
g2.addEdge(0, 1)
g2.addEdge(0, 2)
g2.addEdge(1, 2)
g2.addEdge(2, 0)
g2.addEdge(2, 3)
g2.addEdge(3, 3)
print('Iterative: ', end=' ')
g2.dfsIterative(2)