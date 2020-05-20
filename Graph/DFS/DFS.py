# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

from collections import defaultdict

from collections import OrderedDict
class Graph:

    # Constructor
    def __init__(self):

        # self.graph = defaultdict(list) #adj matrix (dict of lists)
        self.graph = defaultdict(set) # adj list (dict of sets)

        self.visited = set()
        # function to add an edge to graph

    # O(1)
    def addEdge(self, u, v):
        self.graph[u].add(v)


    def dfsRecursive(self, root, visited=set()):
        visited.add(root)
        for v in self.graph[root]:   # Recur for all the vertices adjacent to this vertex
            if v not in visited:
                self.dfsRecursive(v, visited)
        return visited

    def dfsRecursive2(self, root, visited=None):
        if visited == None: visited = set()
        visited.add(root)
        for v in self.graph[root]:   # Recur for all the vertices adjacent to this vertex
            if v not in visited:
                self.dfsRecursive(v, visited)
        return visited

    def dfsIterative(self, v):
        stack = [v]
        while stack:
            vertex = stack.pop()
            if vertex not in self.visited:
                self.visited.add(vertex)
                # print(vertex, end=' ')
                stack.extend(self.graph[vertex] - self.visited) # add unvisited neighbors (set subtraction)
        return self.visited



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

print('Recursive: ', end=' ')
print(g2.dfsRecursive('A'))
print(g2.dfsRecursive2('A'))



# g3 = Graph()
# g3.addEdge(0, 1)
# g3.addEdge(0, 2)
# g3.addEdge(1, 2)
# g3.addEdge(2, 0)
# g3.addEdge(2, 3)
# g3.addEdge(3, 3)
# print(g3.dfsIterative(0))