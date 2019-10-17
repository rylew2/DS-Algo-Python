# Python Program for union-find algorithm to detect cycle in a undirected graph
# we have one egde for any two vertex i.e 1-2 is either 1-2 or 2-1 but not both

from collections import defaultdict


# This class represents a undirected graph using adjacency list representation
class Graph:

    def __init__(self):
        self.graph = defaultdict(set)  # default dictionary to store graph

    def addVertex(self, u):
        self.graph[u]
    # function to add an edge to graph - add both since it's undirected
    def addEdge(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)

    # A utility function to find the subset of an element i
    def find_parent(self, parent, i):
        if parent[i] <= -1: # is this the topmost parent ?
            return i
        else:
            parent[i] = self.find_parent(parent, parent[i]) # path compression
            return parent[i]


    # A utility function to do union of two subsets
    def union(self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[y_set] += parent[x_set] # store rank as negative value in array
        parent[x_set] = y_set



    # The main function to check whether a given graph
    # contains cycle or not
    def isCyclic(self):

        # Allocate memory for creating V subsets and
        # Initialize all subsets as single element sets
        parent = [-1] * len(self.graph) # makeSet() - O(V)

        # Iterate through all edges of graph, find subset of both
        # vertices of every edge, if both subsets are same, then
        # there is cycle in graph.
        visited = set()
        for i in self.graph:
            for j in self.graph[i]:
                if (i,j) not in visited: # prevent cycle detection for the same edge
                    visited.add( (j, i) ); visited.add( (i,j) ); # prevent cycle detection for the same edge
                    x = self.find_parent(parent, i)
                    y = self.find_parent(parent, j)

                    if x == y: print(parent); return True;

                    self.union(parent, x, y)

        print(parent)



g = Graph()
for i in range(5):
    g.addVertex(i)

g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)

# g.addEdge(2, 4)
# g.addEdge(4,0)
g.addEdge(3,4)
# g.addEdge(3,1)

print(g)


if g.isCyclic(): print( "Graph contains cycle")
else: print("Graph does not contain cycle ")

# This code is contributed by Neelam Yadav