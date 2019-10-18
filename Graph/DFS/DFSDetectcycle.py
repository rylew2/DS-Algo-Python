from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(set)

    def addEdge(self, u, v):
        self.graph[u].add(v)

    def addVertex(self,v):
        self.graph[v]

    def dfs_topological_sort(self):
        def tsutil(v, deq, visited):
            visited.add(v)
            for i in self.graph[v]:
                if i not in visited:
                    tsutil(i, deq, visited)

            # append to beginning after we've added all this
            # nodes children
            deq.appendleft(v)

        deq, visited = deque(), set()
        for i in self.graph:
            if i not in visited:
                tsutil(i, deq, visited)

        print(deq)

    def cyclic(self):

        def visit(vertex):
            if vertex in visited: return False
            visited.add(vertex); path.add(vertex);
            for nbor in self.graph[vertex]:
                if nbor in path or visit(nbor):
                    return True
            path.remove(vertex)
            deq.appendleft(vertex)
            return False



        path,visited, deq = set(), set(), deque()
        components = defaultdict(int) #generate number of components
        for v in self.graph:
            if visit(v):
                components[len(visited)] += 1
                # print(components)
                return True
            components[len(visited)] += 1

        print(components)
        return deq



g = Graph()
for i in range(5): g.addVertex(i)
g.addEdge(1,3)
g.addEdge(3,5)
g.addEdge(5,2)
g.addEdge(1,2)
g.addEdge



print(g.cyclic())
# print(g.dfs_topological_sort())