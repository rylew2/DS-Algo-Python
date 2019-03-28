from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(set)

    # O(1)
    def addEdge(self, u, v):

        self.graph[u].add(v)

    # O(1)
    def removeEdge(self, u, v):
        self.graph[u].remove(v)

    # O(1)
    def addVertex(self, v):
        self.graph[v]

    # O(V)
    def removeVertex(self, v):
        del self.graph[v]
        for vert in self.graph:
            if v in self.graph[vert]:
                self.graph[vert].remove(v)
    # O(1)
    def queryEdge(self, u, v ):
        return v in self.graph[u]


    def printGraph(self):
        for v in self.graph:
            print('{} : {}'.format(v, self.graph[v]))


g = Graph()  # space => O(V+E)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.removeEdge(2,3)

g.addVertex(4)
g.addEdge(4,1)
g.addEdge(1,4)

g.removeVertex(4)

if g.queryEdge(0, 2) == True:
    print('0 --> 2 exists', end='\n\n')

g.printGraph()


