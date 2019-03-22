from collections import defaultdict, deque


class Graph:

    def __init__(self):
        self.graph = defaultdict(set) # dictionary of sets
        self.visited = []
        self.q = deque([])


    def addEdge(self, u, v):
        self.graph[u].add(v)

    # recursive
    def bfs(self, root):

        self.visited.append(root)

        for neighbor in self.graph[root]:
            if neighbor not in self.visited:
                self.q.append(neighbor)
                self.visited.append(neighbor)
                print(neighbor)
                # self.bfs(neighbor)

        if self.q:
            self.bfs(self.q.popleft())


        return self.visited


    # Inspired by: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
    def bfs2(self, root):
        print(root)
        self.visited.append(root)
        self.q.append(root)

        while self.q: #continue until queue is empty
            v = self.q.popleft()

            for neighbor in self.graph[v]:
                if neighbor not in self.visited:
                    self.q.append(neighbor)
                    self.visited.append(neighbor)
                    print(neighbor)
        return self.visited

    def reset(self): #reset q and visited, but keep edges
        self.visited = []
        self.q = deque([])

g = Graph()
# g.addEdge(0, 1)
# g.addEdge(1, 2)
# g.addEdge(1, 3)
# g.addEdge(2, 3)
# g.addEdge(0, 4)
# g.addEdge(4,5)
#

g.addEdge(0,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(0,1)
g.addEdge(3,3)

print(2)
g.bfs(2)


print()

g.reset()
g.bfs2(2)


