# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

from collections import defaultdict

from collections import OrderedDict
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph

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
                # print(vertex, end=' ')
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
g2.addEdge('A','B')
g2.addEdge('A','C')
g2.addEdge('B','A')
g2.addEdge('B','D')
g2.addEdge('B','E')
g2.addEdge('C','A')
g2.addEdge('C','F')
g2.addEdge('D','B')
g2.addEdge('E','B')
g2.addEdge('E','F')
g2.addEdge('F','C')
g2.addEdge('F','E')

print('Iterative: ', end=' ')
print(g2.dfsIterative('A'))


g3 = Graph()
g3.addEdge(0, 1)
g3.addEdge(0, 2)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(2, 3)
g3.addEdge(3, 3)
print(g3.dfsIterative(0))