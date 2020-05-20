from collections import defaultdict

class Graph:
    def __init__(self):
        self.g = defaultdict(set) #adjacency list (dict of sets)
        self. visited = set()


    def addEdge(self, u, v):
        self.g[u].add(v)

    def removeEdge(self, u, v):
        self.g[u].remove(v)

    def addVertex(self, v):
        self.g[v] = set()

    def removeVertex(self,v):
        del self.g[v]
        for vert in self.g:
            if v in self.g[vert]:
                self.g[vert].remove(v)

    def printGraph(self):
        for v in self.g:
            print('{} : {}'.format(v, self.g[v]))

    def query(self, u, v):
        return v in self.g[u]


    def dfsRecursive(self, root, visited=None):
        if visited==None: visited = set()
        visited.add(root)
        for v in self.g[root]:
            if v not in visited:
                self.dfsRecursive(v, visited)
        return visited




g = Graph()
g.addEdge(0,1)
g.addEdge(1,0)
g.addEdge(0,2)
g.addEdge(2,0)
g.addEdge(0,3)
g.addEdge(3,0)
g.addEdge(3,1)
g.removeEdge(3,1)

g.addEdge(3,4)
g.addEdge(4,3)
g.addEdge(4,5)
g.addEdge(5,4)

g.addVertex(6)
g.addEdge(5,6)
g.addEdge(6,5)


g.printGraph()
print(g.dfsRecursive(1))





