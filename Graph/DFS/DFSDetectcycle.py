from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(set)

    def addEdge(self, u, v):
        self.graph[u].add(v)

    def addVertex(self,v):
        self.graph[v]

    def cyclic(self):

        def visit(vertex, maxPath):
            if vertex in visited: return False
            visited.add(vertex)
            path.add(vertex)
            maxPath = max(maxPath, len(path))
            print(maxPath)
            for nbor in self.graph[vertex]:
                if nbor in path or visit(nbor, maxPath):
                    return True
            path.remove(vertex)
            return False


        path,visited = set(), set()
        maxPath = 0
        for v in self.graph:
            print(maxPath)
            if visit(v, maxPath): return True


g = Graph()
for i in range(5): g.addVertex(i)
g.addEdge(1,3)
g.addEdge(3,5)
g.addEdge(5,2)
g.addEdge(2,1)



print(g.cyclic())