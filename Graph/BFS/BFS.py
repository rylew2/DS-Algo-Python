from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(set)
        self.visited = set()
        self.q = deque([])

    def addEdge(self, u, v):
        self.graph[u].add(v)

    def bfsIterative(self, v):
        self.q.append(v)
        while self.q:
            vertex = self.q.popleft()
            if vertex not in self.visited:
                print(vertex)
                self.visited.add(vertex)
                self.q.extend(self.graph[vertex] - self.visited)


    def bfsRecursive(self, v):
        self.visited.add(v)
        print(v)
        for i in self.graph[v]:
            if i not in self.visited:
                self.visited.add(i)
                self.q.append(i)
        if self.q:
            self.bfsRecursive(self.q.popleft())





g = Graph()
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(3,6)
g.addEdge(4,7)
g.bfsIterative(1)

print('==================================')
g2 = Graph()
g2.addEdge(1,2)
g2.addEdge(1,3)
g2.addEdge(2,4)
g2.addEdge(2,5)
g2.addEdge(3,6)
g2.addEdge(4,7)
g2.bfsRecursive(1)

